import pandas as pd
import sys
import os
from copy import deepcopy
import streamlit as st
import quantstats as qs
import plotly.graph_objs as go
import plotly.express as px
from Strategy_optimization.sma_cross_strategy import *


SELECT_ASSET_FROM = ['AAPL','GOOG','MSFT']

TRADEABLE_ASSETS = ['AAPL','GOOG','MSFT']

TIME_FRAME = '15Min' #for this strategy, select either H1 or H4

def convert_df_to_csv(df):
    return df.to_csv().encode("utf-8")

def sma_crossover_high_low_signal(row):
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

def load_data(start, end, symbol, time_frame):
    start = pd.to_datetime(start).tz_localize("UTC")
    end = pd.to_datetime(end).tz_localize("UTC")
    #load_data
    base_path = os.path.dirname(__file__)  # directory of current script
    file_path = os.path.join(base_path, "Data", f"{symbol}_{time_frame}.pkl")
    data_df = pd.read_pickle(file_path)
    data_df = data_df.reset_index()
    data_df = data_df[(data_df.time>=start)&(data_df.time<end)]
    data_df = data_df.reset_index().drop(columns=['index'])
    ohlc_data = deepcopy(data_df)
    return ohlc_data

def run_strategy(symbol, start, end, time_frame='15Min',risk_percent=0.5, fast_sma=10, slow_sma=20, lookback=10):
    orig_data = load_data(start, end, symbol, time_frame)
    data = apply_properties(orig_data, symbol,fast_sma,slow_sma, lookback)
    st = StrategyTester(data, sma_crossover_high_low_signal,risk_percent)
    st.run_test()
    return data, st.df_results


def calculate_statistics(returns, data, currency='$'):
    stats = {
        'Sharpe Ratio': round(qs.stats.sharpe(returns, periods=365), 4),
        'Annualized Return': round(qs.stats.cagr(returns, periods=365), 4),
        'Max Drawdown': round(qs.stats.max_drawdown(returns), 4),
        'Volatility': round(qs.stats.volatility(returns, periods=365), 4),
        #'VaR': round(qs.stats.value_at_risk(returns), 4),
        #'CVaR': round(qs.stats.conditional_value_at_risk(returns), 4),
        'Total Number of Trades': len(data),
        '%win': f"{round((data['realised_pnl'] > 0).mean() * 100, 2)}%",
        'Net Profit': f"{currency}{round(data['realised_pnl'].sum(), 2)}",
        'Profit Factor': round(
            data.loc[data['realised_pnl'] > 0, 'realised_pnl'].sum() /
            abs(data.loc[data['realised_pnl'] < 0, 'realised_pnl'].sum())
            if abs(data.loc[data['realised_pnl'] < 0, 'realised_pnl'].sum()) != 0 else float('inf'), 4
        ),
        'Average Trade Net Profit': f"{currency}{round(data['realised_pnl'].mean(), 2)}",
        'Average Time in Trades': f"{round((data['end_time'] - data['start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Avg Time Won Trades': f"{round((data.loc[data['realised_pnl'] > 0, 'end_time'] - data.loc[data['realised_pnl'] > 0, 'start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Avg Time Lost Trades': f"{round((data.loc[data['realised_pnl'] < 0, 'end_time'] - data.loc[data['realised_pnl'] < 0, 'start_time']).mean().total_seconds() / 3600, 2)} hrs",
        'Average Won Trade': f"{currency}{round(data.loc[data['realised_pnl'] > 0, 'realised_pnl'].mean(), 2)}",
        'Average Lost Trade': f"{currency}{round(data.loc[data['realised_pnl'] < 0, 'realised_pnl'].abs().mean(), 2)}",
        'Average Trade Ratio': round(
            data.loc[data['realised_pnl'] > 0, 'realised_pnl'].mean() /
            data.loc[data['realised_pnl'] < 0, 'realised_pnl'].abs().mean(), 4
        )
    }
    
    return stats


if __name__ == '__main__':

    #Define the part of the sidebar used for selecting the ticker and the dates
    
    st.sidebar.header("Stocks Parameters")

    available_assets = TRADEABLE_ASSETS

    #available_cols = df.columns.tolist()
    column_to_show = st.sidebar.radio(
    "Stock",
    available_assets,
    index=0,
    key="Tradeable_Asset"
)

    # Display a non-editable date range in the sidebar
    st.sidebar.write("Date Range: 2022-09-07  -  2025-01-07")

    # Define the part of the sidebar used for tuning the details of the technical analysis
    st.sidebar.header("Technical Analysis Parameters")
    SMA_CROSSOVER_PLUS_BREAKOUT_FILTER = st.sidebar.checkbox(label="Add Breakout Filter", value=True)
    SMA_CROSSOVER_PLUS_BREAKOUT_FILTER = True

    # Add the expander with parameters of the SMA
    fast_sma = st.sidebar.expander("FAST SMA")
    #rsi_flag = exp_rsi.checkbox(label="Add RSI")
    fast_sma_value = fast_sma.number_input(
        label="FAST SMA VALUE", 
        min_value=3, 
        max_value=15, 
        value=10, 
        step=1
    )

    # Add the expander with parameters of the SMA
    slow_sma = st.sidebar.expander("SLOW SMA")
    #rsi_flag = exp_rsi.checkbox(label="Add RSI")
    slow_sma_value = slow_sma.number_input(
        label="SLOW SMA VALUE", 
        min_value=5, 
        max_value=100, 
        value=20, 
        step=1
    )

    # Add the expander with parameters of the lookback parameter
    lookback = st.sidebar.expander("LOOKBACK")
    #rsi_flag = exp_rsi.checkbox(label="Add RSI")
    lookback_value = lookback.number_input(
        label="LOOKBACK VALUE", 
        min_value=5, 
        max_value=100, 
        value=10, 
        step=1
    )
    #add a session for backytest controls
    st.sidebar.header("Backtest Controls")
    risk_percent = st.sidebar.number_input(
        label="RISK (%)", 
        min_value=0.1, 
        max_value=100.0, 
        value=5.0, 
        step=0.1
    )

    risk_decimal = risk_percent / 100.0
    st.sidebar.write(f"Risk as a decimal: {risk_decimal:.5f}")

    # Specify the title and additional text in the app’s main body
    st.title("Backtest analysis for SMA Crossover plus Breakout Filter")


    #create a list and return the result of each strategy by asset
    #results = []
    #for p in column_to_show:
    data, result_dict = run_strategy(column_to_show, start='2022-09-07', end='2025-01-07', time_frame='15Min',risk_percent=risk_decimal, fast_sma=fast_sma_value, slow_sma=slow_sma_value, lookback=lookback_value)
    result_df = pd.DataFrame(result_dict)
    result_df = result_df.sort_values(by='start_time').reset_index(drop=True)


    if 'realised_pnl' in result_df.columns:
        result_df['cumulative_gain'] = result_df['realised_pnl'].cumsum().round(2)


    #make the datafram available on the site
    data_exp = st.expander("Preview data")
    available_cols = result_df.columns.tolist()
    columns_to_show = data_exp.multiselect(
        "Columns", 
        available_cols, 
        default=available_cols,
        key = 'columns_to_download'
    )

    # write to side bar downloaded data
    data_exp.dataframe(result_df)

    csv_file = convert_df_to_csv(result_df)
    data_exp.download_button(
        label="Download selected as CSV",
        data=csv_file,
        file_name="stocks_result_data.csv",
        mime="text/csv",
    )

    # Create a Plotly figure
    fig = px.line(result_df, x='end_time', y='cumulative_gain',color='symbol',title='Cumulative Gain and Close Price')
    # Add close price as secondary y-axis
    fig.add_scatter(x=data['time'],y=data['close'],mode='lines',name='Close Price',line=dict(color='black', dash='dot'),yaxis='y2')
    fig.update_layout(
    yaxis=dict(title='Cumulative Gain'),
    yaxis2=dict(title='Close Price', overlaying='y', side='right'),
    xaxis=dict(title='Time')
)

    # Streamlit app
    st.title('Cumulative Gain & Close Price')
    st.plotly_chart(fig)

    #create table for backtest result
    results_final = {}
    for signal in result_df.sma_signal.unique():
        new_df = result_df[(result_df['sma_signal'] == signal)] 
        new_ret = pd.Series(new_df['returns'].values, index=pd.to_datetime(new_df['end_time']))
        results_final[signal] = calculate_statistics(new_ret, new_df)
    data_return = pd.Series(result_df['returns'].values, index=pd.to_datetime(result_df['end_time']))
    results_final['ALL'] = calculate_statistics(data_return, result_df)


    # Convert results to a DataFrame
    results_df = pd.DataFrame(results_final)#.T.reset_index()
    #results_df.rename(columns={'index': 'Signal'}, inplace=True)

    # Display the results in Streamlit
    st.write(f"Backtest Statistics for {column_to_show}:")
    st.dataframe(results_df)  # Use st.table(results_df) for a static table













