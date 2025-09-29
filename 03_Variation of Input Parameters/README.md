## Variation of the input parameters: optimisation and stability diagrams

Every trading system is in some form an optimization; in choosing any trading system one must have compared it to some others, and proceed to choose it because it shows favorable and predictive results. So the key question is: which set of parameter values works best for the trading system backtest and produces profits in the future in real trading? While the answer to this question is different for every trading system, the one rule that applies to all is that: the neighbourhood or surrounding values of the chosen parameter values must be nearly as profitable as the chosen system parameters, and the bigger this profitable parameter range, the better.

According to Murray Ruggiero, 'If you don’t like the neighbouring numbers, you’ve got a
problem, because odds are, you will wind up with the results of
the neighbouring set of parameters.'

## Strategy Analysis
#### Figure 3.0
<img width="1026" height="470" alt="image" src="https://github.com/user-attachments/assets/6f97ccf4-6ce5-4784-8bce-a6522a418969" />

The SMA crossover strategy produces some positive results on the GOOGLE stock. Indexes close to zero are the initial fast SMA values starting from 1, and slow SMA values starting from 10. The lookback period alternates between 10 and 20 for the sake of simplicity.

With the net profit getting better with increasing index value, it indicates that the strategy works better with higher fast SMA values and higher slow SMA values.

#### Figure 3.1
<img width="1026" height="470" alt="image" src="https://github.com/user-attachments/assets/48bf7349-acb9-40c7-bac6-f3bce6807b00" />

The goal of optimised strategies is to produce parameters with the best results and whose neighboring values produce similar results. This helps to ensure that in the case of changing market conditions, the strategy can still produce positive results. The closest to this is the SMA values within the index range 583 to 590.

#### Figure 3.2: 
<img width="1737" height="580" alt="image" src="https://github.com/user-attachments/assets/b8c2e3c4-7212-4301-9124-7f80e53ecadf" />


Starting from index 584 until 590, the strategy produced results in this order; £1559.47, £1077.51, £1141.02, -£102.74, £2329.85, £374.29, £242.56. For these ones, the SMA values for fast and slow are within the range 16 & 17 for fast SMA and 18,19,20 for slow SMA, while the lookback period alternates between 10 and 20. Unfortunately, this isn't the perfect scenario, but it's somewhat close. So we choose the parameter values as follows:

fast sma value = 17

slow sma value = 20

lookback value = 10

## The Result
#### Figure 3.3: New Equity curve with optimised parameters
<img width="1907" height="907" alt="image" src="https://github.com/user-attachments/assets/70a975d0-9ecb-4627-bf66-1623808f691e" />
#### Figure 3.4: Underwater Drawdown Curve with optimised parameters
<img width="1917" height="900" alt="image" src="https://github.com/user-attachments/assets/4b096c18-f9d2-494e-b906-eed3684d6334" />
#### Table 3.1: Metrics Table of optimised parameters
<img width="1453" height="885" alt="image" src="https://github.com/user-attachments/assets/61543e01-6162-4610-ae73-62d68f05a222" />

With the fast SMA set to 17, the slow SMA set to 20, and the lookback value set to 10, one gets an equity curve on a slightly steadier path than before. This result is confirmed with the underwater drawdown curve  which quickly recovers after every drawdown. The biggest drawdown is 1.56%, which is relatively smaller than 2.7% we achieved earlier in section (2_Commission & slippage Checks) with the non-optimised input parameters (5/10/10).

While the net profit and drawdown amounts of the strategy are an improvement from the previous figures, a closer look at the system figures reveals that the system we have developed to this point cannot be traded yet (Table 3.1.) The system still shows a bias in prices, and the average net profit per trade is only £5, which is not exactly profitable yet.

Additionally, the system is still in the market 100% of the time because the proper and identifiable exit points are still missing. As a consequence, the system is not usable in this state since the risk will be too high compared with the prospective returns. Therefore, the next section (04_Inserting an Intraday time filter) will deal with adding the necessary filters
