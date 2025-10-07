## Determination of Appropriate Exits
The tool of statistical research will be employed to investigate exits quantitatively. Exits cannot be determined independently from the relative entry, neither can exits points be transferable to different entry logic. It is important that one spends the time to develop suitable exits for the different entry or time scale.  This would involve analysing  all single trades taken in the context of the trading strategy and determining useful stop-levels and profit targets. In other words, it involves analysing the distribution of trades and examining each trade individually.

## The use of Maximum Adverse Excursion (MAE)
The Maximum Adverse Excursion (MAE) technique is defined as the most intraday price movement against your position. Put differently, it is the lowest open equity during the lifespan of a trade. This tool enables one to evaluate the trading system's individual trades to determine at what dollar or percentage amount to place the protective stop.

#### Figure 5.1: The MAE graph of SMA crossover system. Green: Profitable trades, red: Losing trades. System tested Google stocks, 15-minute bars, 21/10/2002–4/7/2008, with entry time window 9.45am – 1.15pm ET. Input parameters SLOW=20, FAST=17, LOOKBACK=10. Without exits, always in the market, including on average £10 slippage and commissions per round turn.

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/0349e79c-84b0-453b-aa83-f152af0f8b74" />

The graph above (fig5.1) shows all 227 trades that were taken within the test period. For each trade there is the amount of drawdown that occurred in relation to the realised profit or loss. The profitable trades are shown as green up arrows and the losing trades are represented as red down arrows. The graph aids to figure out how much unrealised loss must be incured by a trade before it typically does not recover. In this way the MAE graph tells you when to cut your loss because the risks associated with the trade are no longer justified. This gives one a valuable indication of where to place the protective stop.

#### Figure 5.2: The MAE graph of SMA crossover system in percentage terms after inserting a 0.5% stop loss. Green: Profitable trades, red: Losing trades. System tested Google stocks, 15-minute bars, 21/10/2002–4/7/2008, with entry time window 9.45am – 1.15pm ET. Input parameters SLOW=20, FAST=17, LOOKBACK=10. Without exits, always in the market, including on average £10 slippage and commissions per round turn.

<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/c812f452-311a-4d56-9a98-ac2251684d41" />

With the MAE graph in percentage terms, we are accounting for the fact that the same dollar movement represents a different percentage change depending on the price level of the market. On the left side of fig 5.2, we find more winning trades than losing trades. This can be attributed to the fact that winning trades usually dont suffer such big drawdowns as losing trades. The best trades are ones that go straight for the win without experiencing any negative open equity.

The loss diagonal alo referred to as the characteristic line are all losing trades, which represent the biggest drawdowns. Beneath this line towards the right side of the graph are trades that suffered drawdowns of over 3.5% from the entry point,very few recovered from this position, while the others completely ended in a loss.

The blue vertical line (fig 5.2) represents a protective stop loss at a distance away from the entry point in order to limit the risk of the trade. On this graph, this vertical line seems to cut all trades that suffer a bigger loss from their entry. This line stops all the trades at 0.3£ of entry price,that eventually ended in a loss.There is also a tradeoff of trades that turned into a profit beyond this point. Going lower than this would lead to cutting trades that recovered from drawdowns into a profit.

## Looking for profit targets: Maximum Favourable Excursion (MFE)

#### Figure 5.3: The MFE graph of SMA crossover system in percentage terms after inserting. Green: Profitable trades, red: Losing trades. System tested Google stocks, 15-minute bars, 21/10/2002–4/7/2008, with entry time window 9.45am – 1.15pm ET. Input parameters SLOW=20, FAST=17, LOOKBACK=10. Without exits, always in the market, including on average £10 slippage and commissions per round turn
<img width="989" height="590" alt="image" src="https://github.com/user-attachments/assets/e513c0a0-780d-41ab-8cde-00af56dff54b" />


