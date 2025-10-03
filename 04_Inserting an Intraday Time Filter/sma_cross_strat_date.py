import pandas as pd
import sys
import os
from copy import deepcopy
import pytz
#import streamlit as st
import quantstats as qs
from datetime import datetime, time, timedelta, date
#import plotly.express as px
from Strategy_optimization.sma_cross_strat_date import *


SELECT_ASSET_FROM = ['AAPL','GOOG','MSFT']

TRADEABLE_ASSETS = ['AAPL','GOOG','MSFT']

TIME_FRAME = '15Min' #for this strategy, select either H1 or H4

def convert_df_to_csv(df):
    return df.to_csv().encode("utf-8")

def sma_crossover(row):
    if row.fast_sma > row.slow_sma and row.close > row.prev_highest:
        return 'BUY'
    elif row.fast_sma < row.slow_sma and row.close < row.prev_lowest:
        return 'SELL'
    return None

def apply_properties(df:pd.DataFrame, symbol, fast_sma,slow_sma, lookback):
    ohlc_data = df.copy()
    ohlc_data['next_open'] = ohlc_data['open'].shift(-1)
    ohlc_data['open_date'] = ohlc_data['time'].shift(-1)
    ohlc_data['symbol'] = symbol
    ohlc_data['fast_sma'] = ohlc_data['close'].rolling(fast_sma).mean()
    ohlc_data['slow_sma'] = ohlc_data['close'].rolling(slow_sma).mean()
    ohlc_data['prev_highest'] = ohlc_data['close'].shift(1).rolling(lookback).max()
    ohlc_data['prev_lowest'] = ohlc_data['close'].shift(1).rolling(lookback).min()
    ohlc_data = ohlc_data.dropna()
    ohlc_data = ohlc_data.reset_index(drop=True)
    return ohlc_data


def load_data(start, end, symbol, time_frame='15Min'):
    data_df = pd.read_pickle(f'./Data/{symbol}_{time_frame}.pkl')
    data_df = data_df.reset_index()

    # Convert data timestamps from UTC to US/Eastern
    eastern = pytz.timezone('US/Eastern')
    data_df['time'] = data_df['time'].dt.tz_convert(eastern)

    start = eastern.localize(pd.Timestamp(start))
    end   = eastern.localize(pd.Timestamp(end))
    
    data_df = data_df[(data_df.time>=start)&(data_df.time<end)]
    data_df = data_df.reset_index().drop(columns=['index'])
    ohlc_data = deepcopy(data_df)
    return ohlc_data

def run_strategy(symbol, start, end, start_t, end_t, time_frame='15Min',risk_percent=5, fast_sma=10, slow_sma=20, lookback=10,add_comm_slipp=True, commission_per_share=0.05, slippage_per_share=0.003):
    orig_data = load_data(start, end, symbol, time_frame)
    data = apply_properties(orig_data, symbol,fast_sma,slow_sma, lookback)
    st = StrategyTester(data, sma_crossover,risk_percent, start_t, end_t,add_comm_slipp, commission_per_share, slippage_per_share)
    st.run_test()
    return data, st.df_results


def calculate_statistics(returns, data, currency='£'):
    stats = {
        'Sharpe Ratio': round(qs.stats.sharpe(returns, periods=365), 4),
        'Annualized Return': round(qs.stats.cagr(returns, periods=365), 4),
        'Max Drawdown': round(qs.stats.max_drawdown(returns), 4),
        'Volatility': round(qs.stats.volatility(returns, periods=365), 4),
        #'VaR': round(qs.stats.value_at_risk(returns), 4),
        #'CVaR': round(qs.stats.conditional_value_at_risk(returns), 4),
        'Total Number of Trades': len(data),
        '%win': f"{round((data['net_pnl'] > 0).mean() * 100, 2)}%",
        'Net Profit': f"{currency}{round(data['net_pnl'].sum(), 2)}",
        'Profit Factor': round(
            data.loc[data['net_pnl'] > 0, 'net_pnl'].sum() /
            abs(data.loc[data['net_pnl'] < 0, 'net_pnl'].sum())
            if abs(data.loc[data['net_pnl'] < 0, 'net_pnl'].sum()) != 0 else float('inf'), 4
        ),
        'Average Trade Net Profit': f"{currency}{round(data['net_pnl'].mean(), 2)}",
        'Average Time in Trades': f"{round((data['end_time'] - data['start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Avg Time Won Trades': f"{round((data.loc[data['net_pnl'] > 0, 'end_time'] - data.loc[data['net_pnl'] > 0, 'start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Avg Time Lost Trades': f"{round((data.loc[data['net_pnl'] < 0, 'end_time'] - data.loc[data['net_pnl'] < 0, 'start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Average Won Trade': f"{currency}{round(data.loc[data['net_pnl'] > 0, 'net_pnl'].mean(), 2)}",
        'Average Lost Trade': f"{currency}{round(data.loc[data['net_pnl'] < 0, 'net_pnl'].abs().mean(), 2)}",
        'Average Trade Ratio': round(
            data.loc[data['net_pnl'] > 0, 'net_pnl'].mean() /
            data.loc[data['net_pnl'] < 0, 'net_pnl'].abs().mean(), 4
        )
    }
    
    return stats



def run_symbol(symbol,risk_percent,start='2022-09-07', end='2025-01-07',add_comm_slipp=True, time_frame='15Min'):
    comm=0.05
    slipp=0.03
    risk_decimal = float(risk_percent)/100
    metrics_final= []
    fsv = 17
    ssv = 20
    lbv = 10

    start_dt = pd.to_datetime(start)   # convert once here
    end_dt   = pd.to_datetime(end)
    window_start = time(5,0)
    window_end = (datetime.combine(start_dt.date(), window_start) + timedelta(hours=4)).time()

    while window_end <= time(18,59):
        print(window_start, window_end)
        _, result_dict = run_strategy(symbol, start=start, end=end,start_t=window_start, end_t=window_end, time_frame=time_frame,risk_percent=risk_decimal, fast_sma=fsv, slow_sma=ssv, lookback=lbv,add_comm_slipp=add_comm_slipp, commission_per_share=comm, slippage_per_share=slipp)
        result_df = pd.DataFrame(result_dict)
        if result_df.empty:
            window_start = (datetime.combine(start_dt.date(), window_start) + timedelta(minutes=15)).time()
            window_end = (datetime.combine(end_dt.date(), window_start) + timedelta(hours=4)).time()
            continue
        result_df = result_df.sort_values(by='start_time').reset_index(drop=True)

        if 'net_pnl' in result_df.columns:
            result_df['cumulative_gain'] = result_df['net_pnl'].cumsum().round(2)
    
        #create table for backtest result
        data_return = pd.Series(result_df['returns'].values, index=pd.to_datetime(result_df['end_time']))
        metrics = calculate_statistics(data_return, result_df)
        metrics.update({'start_time':window_start, 'end_time':window_end,'commission_per_share':comm,'slippage_per_share':slipp,'symbol':symbol})
        print(metrics)
        metrics_final.append(metrics)

        #shift by 15 minutes
        window_start = (datetime.combine(start_dt.date(), window_start) + timedelta(minutes=15)).time()
        window_end = (datetime.combine(end_dt.date(), window_start) + timedelta(hours=4)).time()
        #print(metrics)

        # Convert results to a DataFrame
    results_df = pd.DataFrame(metrics_final)#.T.reset_index()
    #print(results_df)
                
    return results_df

def run_sma_crossover():
    results_df = []
    symbol_list = ['AAPL','GOOG','MSFT']
    save_dir = './exploration/sma_crossover_entry_time'
    os.makedirs(save_dir, exist_ok=True)
    for symbol in symbol_list:
        results_df = run_symbol(symbol, risk_percent=1)
        results_df.to_pickle(f'{save_dir}/metrics_{symbol}.pkl')

if __name__ == '__main__':

    run_sma_crossover()
    #load_data(start='2022-09-07', end='2025-01-07', symbol='AAPL')

    

















