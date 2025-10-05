## Inserting an Intraday Time Filter
Different Trading strategies exploit different phases of the market within the trading day. Some trading strategies are more successful in the afternoon with short-term breakout strategies, while some might require running the whole night in order to make a profit. Timing trade entry becomes increasingly important because markets are controlled by people, and people in turn, operate on daily schedules. Stocks trade on a single local exchange schedule (e.g., NYSE: 09:30–16:00 ET). During market open (first 30–60 mins), there is very high volume & volatility. Lots of institutional orders hitting, and gaps resolving, which is good for short-term breakout strategies. During the midday (11:00–14:00 ET), market is quiet, and there is low volume. Mean-reversion/market-making strategies work better here while trend-following usually fails. At market close (last 1–2 hours), volume rises again, institutions adjust positions, and there are closing auctions. Breakout/trend strategies can work. As a direct consequence, it is worth examining how different time filters change the outcome of the trading strategy.

## Finding the best Entry Time
To determine the best trading time, the trading strategy is restricted to a four hour trading window everyday. Then the starting time of the trading window is shifted in steps of 15 minutes throughout the day in order to find the best window. The result indicated by figure 4.1 which shows the net profit of the trading system as a function of the starting time of the four-hour time window. The time period 9:45 am until 13:13pm ET is the most profitable time range, whereas, the system loses money across other time ranges.

Regarding the issue of stability and robustness of input parameters, it is very important to have a good and broad neighborhood parameters for one's chosen system parameters. This increases the likelihood of conforming to backtest result in real trading. In our case, the neighborhood parameters of the 9:45am to 13:15pm arent the best, they perform quite poorly. However, we can work with this range and optimize further to ascertain if we can produce better results.


#### Figure 4.1: Total Net profit as a function of the starting time of the four-hour time window. Google stock. 2022-09-07 - 2025-01-07.
<img width="1023" height="587" alt="image" src="https://github.com/user-attachments/assets/4bec8687-cb80-4c23-8c71-0f5068d81ea9" />

## Results with Added Filter
The equity curve has changed slightly due to the time filter applied (fig 4.1). However, the drawdown curve shows the most improvement, as there is an evident reduction from 1.56% to a 1.23% in maximum drawdown (fig4.4). The trade count reduced to 227 in the whole of 5 years from a count of 390. The system still takes time to recover from a drawdown. The total net profit reduced from £2329.85 to £1979.03. In terms of the greatest improvement, these would be the slight increases in profit factor and the Average trade ratio, and the reduction in the maximum drawdown. The profit factor increased from 1.15 to 1.17, while the Average trade ratio increased from 1.69 to 1.89, very close to 2 (fig4.4).

So far, the biggest weakness of the trading system is that trade reversals are only allowed in the approximately four-hour trading window. 9:45am - 1:15pm ET. If there is a signal for reversal outside of this range, since the market is closed, the system cannot exit or reverse
its position. Outside of your trading window, you have to stay in the market for the other 20 hours, regardless of what happens.

Leaving the trading strategy in this form would be dangerous and unacceptable; hence, we can change this situation and extend the trading system by adding exits. This aids in creating not just a profitable trading strategy, but one  that can be controlled in terms of risk. 

#### Figure 4.2 SMA Crossover system with added time filter. Entries only allowed in the four-hour time window from 9:45am-1:15pm ET. Detailed Equity curve of the Google stock, 15 minutes bars,  2022-09-07 - 2025-01-07. Optimised input parameters in terms of net profit: SLOW=20, FAST=17, LOOKBACK=10. Test without exits. Back-test includes on average £10 slippage and commission
<img width="1732" height="117" alt="image" src="https://github.com/user-attachments/assets/5830958b-ebcb-46c6-aae2-3775a154b179" />
<img width="1915" height="917" alt="image" src="https://github.com/user-attachments/assets/740b7c29-ae32-4d85-a791-cb375e6c869c" />

#### Figure 4.3 SMA Crossover system with added time filter. Entries only allowed in the four-hour time window from 9:45am-1:15pm ET. Detailed Drawdown curve of the Google stock, 15-minute bars,  2022-09-07 - 2025-01-07. Optimised input parameters in terms of net profit: SLOW=20, FAST=17, LOOKBACK=10. Test without exits. Back-test includes on average £10 slippage and commission
<img width="1918" height="803" alt="image" src="https://github.com/user-attachments/assets/9fa0224c-89c6-4339-99e9-2fc4e07b3d81" />

#### Figure 4.4 SMA Crossover system with added time filter. Entries only allowed in the four-hour time window from 9:45 am-1:15 pm ET. Detailed Metrics table of the Google stock, 15-minute bars,  2022-09-07 - 2025-01-07. Optimised input parameters in terms of net profit: SLOW=20, FAST=17, LOOKBACK=10. Test without exits. Back-test includes on average £10 slippage and commission
<img width="1515" height="756" alt="image" src="https://github.com/user-attachments/assets/58dbb0da-1b79-4532-bafa-06a75fefdb08" />

The next section for improvement is the 05_Determination of appropriate exits. The risk management apsect of the trading system
## Link to Dashboard 
https://trading-sytem-creation-and-optimization.streamlit.app/


