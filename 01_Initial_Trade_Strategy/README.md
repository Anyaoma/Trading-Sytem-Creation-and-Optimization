## First Evaluation of the Trading System; without Slippage and Commission

The strategy is applied to the 15-minute GOOGLE (MSFT, AAPL) stock data from 2022-09-07 - 2025-01-07. To keep the initial analysis very simple, the trading system's results are calculated without adding the commission and the slippage amounts. This will be added in the next section, where their impact on system performance will be analysed. Also, the strategy is structured to include just entries and trade reversals, leaving out exits (the strategy is always in the market, either buying or selling).

As first input parameters for the trading system, we choose 5 bars for the fast SMA, 10 bars for the slow SMA, and 20 bars for the lookback period (maximum - for a buy - or minimum - for a sell - close price in the previous 20 bars). With 15-minute bars this means the fast SMA is calculated from the last 1 hour and 15 minutes, whereas the slow SMA relies on the last 2 hours and 30 minutes, and the lookback relies on the previous 5 hours. The figure below shows the resulting equity curve (cumulative gain over time) in a detailed form; the run ups and drawdowns of the trades which happened during its lifetime.

<img width="1916" height="943" alt="image" src="https://github.com/user-attachments/assets/17e83b90-dbd9-441b-bc33-4143dcf7b6fe" />


The equity line of this strategy looks like a manageable starting point for a viable trading system. There are large drawdowns evident at specific points and time, although the system recovers steadily, resulting in the steady growth of the initial capital. The figure below reveals the somewhat profitable nature of the strategy. A total netprofit amount of £2,357.78 from mid 2022 to mid 2025. This is a fairly profitable strategy where the average risk amount for every trade is £5000 (5% of equity). The biggest drawdown within this period was £

<img width="1568" height="926" alt="image" src="https://github.com/user-attachments/assets/863c6214-945e-4f4f-8d70-7e8431b41598" />








## Link to the Trade Dashboard
https://trading-sytem-creation-and-optimization.streamlit.app/
