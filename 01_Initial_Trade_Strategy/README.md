## First Evaluation of the Trading System; without Slippage and Commission

The strategy is applied to the 15-minute GOOGLE (MSFT, AAPL) stock data from 2022-09-07 - 2025-01-07. To keep the initial analysis very simple, the trading system's results are calculated without adding the commission and the slippage amounts. This will be added in the next section, where their impact on system performance will be analysed. Also, the strategy is structured to include just entries and trade reversals, leaving out exits (the strategy is always in the market, either buying or selling).

As first input parameters for the trading system, we choose 5 bars for the fast SMA, 10 bars for the slow SMA, and 20 bars for the lookback period (maximum - for a buy - or minimum - for a sell - close price in the previous 20 bars). With 15-minute bars this means the fast SMA is calculated from the last 1 hour and 15 minutes, whereas the slow SMA relies on the last 2 hours and 30 minutes, and the lookback relies on the previous 5 hours. The figure below shows the resulting equity curve (cumulative gain over time) in a detailed form; the run ups and drawdowns of the trades which happened during its lifetime.

<img width="1916" height="943" alt="image" src="https://github.com/user-attachments/assets/17e83b90-dbd9-441b-bc33-4143dcf7b6fe" />


The equity line of this strategy looks like a manageable starting point for a viable trading system. There are large drawdowns evident at specific points and time, although the system recovers steadily, resulting in the steady growth of the initial capital. The figure below reveals the somewhat profitable nature of the strategy. A total net profit amount of £2,357.78 from mid-2022 to mid-2025. This is a fairly profitable strategy where the average risk amount for every trade is £5000 (5% of equity) with a starting account balance of £100,000. The biggest drawdown (on an account balance basis) within this period was -0.0238 (-2.38% of total account balance, which equals £2,380). With a starting capital of £100,000, and 5% invested in each trade, we achieved 2.4% over the test horizon. This makes it a conservative but positive-expectancy system, and a foundation that could potentially be enhanced with position sizing adjustments, diversification, or strategy refinements. A note of worry is definitely a maximum drawdown amount equating to the total return.

<img width="1485" height="922" alt="image" src="https://github.com/user-attachments/assets/24a0ba96-2bd3-4fb2-bdd8-07da78ff453b" />




The diagram above shows the main properties of the trend following strategy:

1. The total percentage of profitable trades is 39%, which is low. From a total of 443 trades taken, 172 trades came out profitable, whereas the majority (271) ended in a loss.
2. The average trade ratio, which divides the average win by the average loss is high (1.7807). The average winning trade is £102.81, which is bigger than the average losing trade of £57.734.
3. The average time in won trades is almost three times (70.26 hours) longer than the average time the system stays in lost trades 30.57hours). Which in some way follows the rule that; cut the losses short and let the profits run.

Also evident is the fact that the long side of the trading system is much more profitable than the short side (£2930.63 vs -£572.85) net profit. Markets often have a bias. In the case of equity (stocks rise over decades), the long-term bias is upward. Because of this, systems that go long tend to perform better than systems that go short. The short  trades are in the losing range, which questions the symmetricality of the trading system. Although the difference in net profit between the long and short trades is £3503.48.

In terms of the total number of trades taken on both sides, they are nearly the same, with long trades being 222 and short trades being 221. This is because the trading system only reverses positions for now. No exits have been added to the strategy, so the system stays in the market 100% of the time, holding either a long or short position.

So far, the strategy only produces a total number os 443 trades, which might indicate that the probability of achieving profitable results just by accident is high. Total trades around 2000+ might suffice to indicate future performance.

So far, statistics show that the entry logic would need a bit of tweaking. The probability of maintaining similar performance or behaviour in the future isn't that high. Additionally, the the average profit per trade is only £










## Link to the Trade Dashboard
https://trading-sytem-creation-and-optimization.streamlit.app/
