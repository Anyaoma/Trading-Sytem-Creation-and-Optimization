import pandas as pd


#if stop loss formular, write

#if take profit formular, write


def process_signal(df:pd.DataFrame, trade_signal):
    df['sma_signal'] = df.apply(trade_signal, axis=1)
    return df
    
def in_time_window(row, start_time, end_time):
    return start_time <= row.time.time() < end_time


class Trade:
    def __init__(self, row):
        self.running = True
        self.symbol = row.symbol
        self.sma_signal = row.sma_signal
        self.open_price = row.next_open

        self.end_time = None
        self.start_time = row.open_date

    def close_trade(self, row, trigger_price):
        self.running = False
        self.end_time = row.open_date
        self.close_price = trigger_price

        if self.sma_signal == 'BUY':
            self.price_difference = self.close_price - self.open_price
        elif self.sma_signal == 'SELL':
            self.price_difference = self.open_price - self.close_price

        self.result = 'PROFIT' if self.price_difference > 0 else 'LOSS'

  
    def update_trade(self, row):
        if self.sma_signal == 'BUY' and row.sma_signal == 'SELL':
            self.close_trade(row, row.next_open)
            return 'FLIP'
           
        elif self.sma_signal == 'SELL' and row.sma_signal == 'BUY':
            self.close_trade(row, row.next_open)
            return 'FLIP'
        return None
           


class StrategyTester:

    def __init__(self, df:pd.DataFrame, trade_signal,  risk_percent, start_t=None, end_t=None, add_comm_slipp=True, commission_per_share=0.05, slippage_per_share=0.003):
            self.data = df.copy()
            self.trade_signal = trade_signal
            self.risk_percent = risk_percent
            self.start_t= start_t
            self.end_t = end_t
            pnl_list = []

            self.initial_amount = 100000
            self.amount = self.initial_amount
            self.units = 0

            self.realised_pnl = []
            self.closed_trades = []
            self.open_trade = None

            if add_comm_slipp:
                self.commission_per_share = commission_per_share
                self.slippage_per_share = slippage_per_share
            else:
                self.commission_per_share = 0.0
                self.slippage_per_share = 0.00

            self.prepare_data()

    def prepare_data(self):
        print('preparing data...')

        self.data = process_signal(self.data, 
                        self.trade_signal)
        
    def calculate_risk_amount(self):
        self.risk_amount = self.risk_percent * self.amount

    def calculate_unit(self,row):
        self.calculate_risk_amount()
        self.units = self.risk_amount/row.next_open

    def calculate_commission_cost(self):
        return self.units * self.commission_per_share * 2

    def calculate_slippage_cost(self):
        return self.units * self.slippage_per_share * 2
        
    def calculate_returns(self,net_pnl, starting_balance):
        self.returns = net_pnl/starting_balance

    def update_account_balance(self, net_pnl):
        self.amount += net_pnl

    def run_test(self):
        print('run_test...')

        for _, row in self.data.iterrows():
            if self.open_trade and in_time_window(row, self.start_t, self.end_t):
                action = self.open_trade.update_trade(row)

                if not self.open_trade.running: #if trade is closed
                    commission_cost = self.calculate_commission_cost()
                    slippage_cost = self.calculate_slippage_cost()
                    gross_pnl = self.units * self.open_trade.price_difference
                    net_pnl = gross_pnl - (commission_cost + slippage_cost)
                    starting_balance = self.amount
                    self.calculate_returns(net_pnl,starting_balance)
                    self.update_account_balance(net_pnl)
                    
                    self.open_trade.account_balance = round(self.amount,2)
                    self.open_trade.gross_pnl = round(gross_pnl,2)
                    self.open_trade.commission_cost = round(commission_cost,2)
                    self.open_trade.slippage_cost = round(slippage_cost,2)
                    self.open_trade.net_pnl = round(net_pnl,2)
                    self.open_trade.returns = round(self.returns,5)
                    pnl_list.append(round(net_pnl,2))
                    self.open_trade.running_pnl = pnl_list
                    self.closed_trades.append(self.open_trade)
                    
                    if action == 'FLIP':
                        # immediately open the opposite trade
                        self.calculate_unit(row)
                        self.open_trade = Trade(row)
                        self.open_trade.risk_amount = round(self.risk_amount,2)
                        pnl_list = []
        
                else:
                    commission_cost = self.calculate_commission_cost()
                    slippage_cost = self.calculate_slippage_cost()
                    if self.open_trade.sma_signal == 'BUY':
                        unrealised_pnl = self.units * (row.close - self.open_trade.open_price) - (commission_cost + slippage_cost)
                        
                    else:
                        unrealised_pnl = self.units * (self.open_trade.open_price - row.close) - (commission_cost + slippage_cost)
                    pnl_list.append(round(unrealised_pnl,2))
            
            elif self.open_trade and not in_time_window(row, self.start_t, self.end_t):
                commission_cost = self.calculate_commission_cost()
                slippage_cost = self.calculate_slippage_cost()
                if self.open_trade.sma_signal == 'BUY':
                    unrealised_pnl = self.units * (row.close - self.open_trade.open_price) - (commission_cost + slippage_cost)
                        
                else:
                    unrealised_pnl = self.units * (self.open_trade.open_price - row.close) - (commission_cost + slippage_cost)
                pnl_list.append(round(unrealised_pnl,2))
            
            else:
                # flat, no open trade
                if row.sma_signal in ['BUY', 'SELL'] and in_time_window(row, self.start_t, self.end_t):
                    self.calculate_unit(row)
                    self.open_trade = Trade(row)
                    self.open_trade.risk_amount = round(self.risk_amount,2)
                    pnl_list = []

          # results DataFrame
        #self.df_results = pd.DataFrame([vars(t) for t in self.closed_trades])
        self.df_results = pd.DataFrame.from_dict([vars(x) for x in self.closed_trades]) 

        return self.df_results








