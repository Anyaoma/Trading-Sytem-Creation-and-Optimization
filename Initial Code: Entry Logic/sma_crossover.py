import numpy as np
import pandas as pd
from copy import deepcopy
from KPI_Metrics import *
import matplotlib.pyplot as plt

class BacktestBase:
    def __init__(self, symbol, start, end, time_frame='15Min', amount=10000, ftc=0.0, ptc=0.0):
        self.position = 0
        self.trade = 0
        self.units = 0
        self.start = start
        self.end = end
        self.initial_amount = amount
        self.amount = self.initial_amount
        self.ptc = ptc
        self.ftc = ftc
        self.time_frame = time_frame
        self.symbol = symbol
        self.long_data = {}
        self.short_data = {}
        self.get_data()

    def get_data(self):
        start = pd.to_datetime(self.start).tz_localize("UTC")
        end = pd.to_datetime(self.end).tz_localize("UTC")

        #load_data
        data_df = pd.read_pickle(f'./Data/{self.symbol}_{self.time_frame}.pkl')
        data_df = data_df.reset_index()
        data_df = data_df.reset_index()
        data_df = data_df[(data_df.time>=start)&(data_df.time<end)]
        ohlc_data = deepcopy(data_df)
        ohlc_data['return'] = np.log(ohlc_data['close']/ohlc_data['close'].shift(1))
        ohlc_data['next_open'] = ohlc_data['open'].shift(-1)
        ohlc_data['open_date'] = ohlc_data['time'].shift(-1)
        ohlc_data = ohlc_data.reset_index(drop=True)
        self.data = ohlc_data.dropna()
        return ohlc_data
    
    def plot_data(self, symbol,cols=None):
        if cols is None:
            cols = ['close']
        plt.plot(self.data['time'], self.data[cols])
        plt.xlabel('price')
        plt.ylabel('Date')
        plt.title(f'{symbol} close price')
        plt.show()
        

    def get_date_and_price(self, bar):
        date = str(self.data['open_date'].iloc[bar])[:10]
        price = self.data['next_open'].iloc[bar]
        return date, price

    def place_buy_trade(self, bar, units=None, amount=None):
        date, price = self.get_date_and_price(bar)
        if units is None:
            units = amount/price
        self.amount -= units*price * (1 + self.ptc) + self.ftc
        self.units += 1
        self.trade += 1

    def place_sell_trade(self, bar, units=None, amount=None):
        date, price = self.get_date_and_price(bar)
        if units is None:
            units = amount/price
        self.amount += units*price *  (1 - self.ptc) - self.ftc
        self.units -= units
        self.trade += 1

    def close_out(self, bar):
        date, price = self.get_date_and_price(bar)
        self.amount += self.units * price
        self.units = 0
        #perf = ((self.amount - self.initial_amount)/self.initial_amount)*100



class LongShortBacktest(BacktestBase):
    def __init__(self, symbol, start, end,time_frame='15Min', amount=10000, ftc=0.0, ptc=0.0):
        super().__init__(symbol, start, end,time_frame='15Min', amount=10000, ftc=0.0, ptc=0.0)


    def go_long(self, bar, units=None, amount=None):
        if self.position ==-1: #if existing trade is a sell and a buy condition has alligned, 
            self.short_data[self.trade].append(self.data['next_open'].iloc[bar])
            self.place_buy_trade(bar, units=-self.units)  #take a sell trade with the same unit as the sell trade to close the trade
        if units:      #if unit amount is available, run the code below           
            self.place_buy_trade(bar, units)
            self.long_data[self.trade] = [self.data['next_open'].iloc[bar]]
        elif amount:   #however, idfthe amount is availbale , run the code below
            if amount == 'all':
                amount = self.amount
            self.place_buy_trade(bar, amount=amount)
            self.long_data[self.trade] = [self.data['next_open'].iloc[bar]]

    def go_short(self, bar, units=None, amount=None):
        if self.position == 1:
            self.long_data[self.trade].append(self.data['next_open'].iloc[bar])
            self.place_sell_trade(bar, units=self.units)
        if units:
            self.place_sell_trade(bar, units=units)
            self.short_data[self.trade] = [self.data['next_open'].iloc[bar]]
        elif amount:
            if amount == 'all':
                amount = self.amount
            self.place_sell_trade(bar, amount=amount)
            self.short_data[self.trade] = [self.data['next_open'].iloc[bar]]

    def run_sma_strategy(self, SMA1, SMA2, lookback):
        msg = f'\n\nRunning SMA strategy | SMA1={SMA1} & SMA2={SMA2}'
        msg += f'\nfixed costs {self.ftc} | '
        msg += f'proportional costs {self.ptc}'
        print(msg)
        print('=' * 55)

        self.position = 0
        self.trade = 0
        self.amount = self.initial_amount
        self.long_data = {}
        self.short_data = {}

        self.data['SMA1'] = self.data['close'].rolling(SMA1).mean()
        self.data['SMA2'] = self.data['close'].rolling(SMA2).mean()
        self.data['rolling_high'] = self.data['close'].shift(1).rolling(lookback).max()
        self.data['rolling_low'] = self.data['close'].shift(1).rolling(lookback).min()

        for bar in range(max(SMA2,lookback), len(self.data)):
            if self.position in [0, -1]:
                if self.data['SMA1'].iloc[bar] > self.data['SMA2'].iloc[bar] and self.data['close'].iloc[bar] > self.data['rolling_high'].iloc[bar]:
                    self.go_long(bar, amount='all')
                    self.position = 1
            if self.position in [0,1]:
                if self.data['SMA1'].iloc[bar] < self.data['SMA2'].iloc[bar] and self.data['close'].iloc[bar] < self.data['rolling_low'].iloc[bar]:
                    self.go_short(bar, amount='all')
                    self.position = -1 
        self.close_out(bar)
        if self.trade % 2 != 0:
            for trade in self.long_data:
                if len(self.long_data[trade]) == 1:
                    self.long_data[trade].append(self.data['close'].iloc[bar])
            for trade in self.short_data:
                if len(self.short_data[trade]) == 1:
                    self.short_data[trade].append(self.data['close'].iloc[bar])
        
    def build_trade_history(self):
        trade_records = []
        #process longs
        for trade_id, values in self.long_data.items():
            if len(values) == 2:
                entry, exit_ = values
                returns = exit_/entry
                trade_records.append({'trade_id':trade_id, 'direction':'long','entry':entry,'exit':exit_,'return':returns})
        #process shorts
        for trade_id, values in self.short_data.items():
            if len(values) == 2:
                entry, exit_ = values
                returns = entry/exit_
                trade_records.append({'trade_id':trade_id, 'direction':'short','entry':entry,'exit':exit_,'return':returns})

        df = pd.DataFrame(trade_records).sort_values("trade_id").reset_index(drop=True)
        df['cumulative_return'] = df['return'].cumprod()
        self.return_df = df
        print(self.return_df)
        return df
    

    def print_overall_return(self, symbol):
        total_return = self.return_df['return'].cumprod().iloc[-1]- 1
        print(f"Total return {symbol} = {total_return:.2%}")
        #return total_return
    
    def plot_overall_return(self, cols=None):
        plt.plot(self.return_df['trade_id'], self.return_df['cumulative_return'])
        plt.xlabel('Trade #')
        plt.ylabel('Equity Curve')
        plt.title('Cumulative Returns')
        plt.show()
    

    def calculate_intra_day_KPI(self,symbol):        
        print("calculating intraday KPIs for")
        ret_df = self.return_df
        win_rate = winRate(ret_df) #win rate
        mean_ret_pt =  meanretpertrade(ret_df) #mean return per trade
        mean_ret_pwt =  meanretwintrade(ret_df) #mean return per winning trade
        mean_ret_plt =  meanretlostrade(ret_df) #mean return per lost trades
        max_cons_loss =  maxconsectvloss(ret_df) #maximum consecutive loss
        max_drawdown = max_dd(ret_df)

        KPI_df = pd.DataFrame([win_rate,mean_ret_pt,mean_ret_pwt,mean_ret_plt,max_cons_loss,max_drawdown],
                      index=["Win Rate","Mean Return Per Trade","MR Per WR", "MR Per LR", "Max Cons Loss",'Max Drawdown'])  
        self.KPI_df = KPI_df.T
        self.KPI_df.index = [symbol]
        print(f'{self.KPI_df}')

    





                
                        

                    

            


        


    
   
        

