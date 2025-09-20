## First Evaluation of the Trading System; without Slippage and Commission

The strategy is applied to the 15-minute GOOGLE (MSFT, AAPL) stock data from 2022-09-07 - 2025-01-07. To keep the initial analysis very simple, the trading system's results are calculated without adding the commission and the slippage amounts. This will be added in the next section, where their impact on system performance will be analysed. Also, the strategy is structured to include just entries and trade reversals, leaving out exits (the strategy is always in the market, either buying or selling).

As first input parameters for the trading system, we choose 5 bars for the fast SMA, 10 bars for the slow SMA, and 20 bars for the lookback period (maximum - for a buy - or minimum - for a sell - close price in the previous 20 bars). With 15-minute bars this means the fast SMA is calculated from the last 1 hour and 15 minutes, whereas the slow SMA relies on the last 2 hours and 30 minutes, and the lookback relies on the previous 5 hours. The figure below shows the resulting equity curve (cumulative gain over time) in a detailed form; the run ups and drawdowns of the trades which happened during its lifetime.

<img width="1892" height="970" alt="image" src="https://github.com/user-attachments/assets/4f2bd848-b6e4-4fa2-b675-d99c5c449dd1" />


The equity line of this strategy looks like a manageable starting point for a viable trading system. There are large drawdowns evident at specific points and time, although the system recovers steadily and sometimes quickly resulting in the steady growth of the initial capital. 







## Linl to the Trade Dashboard
https://trading-sytem-creation-and-optimization.streamlit.app/
