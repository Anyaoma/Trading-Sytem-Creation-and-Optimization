## Variation of the input parameters: optimisation and stability diagrams

Every trading system is in some form an optimization; in choosing any trading system one must have compared it to some others, and proceed to choose it because it shows favorable and predictive results. So the key question is: which set of parameter values works best for the trading system backtest and produces profits in the future in real trading? While the answer to this question is different for every trading system, the one rule that applies to all is that: the neighbourhood or surrounding values of the chosen parameter values must be nearly as profitable as the chosen system parameters, and the bigger this profitable parameter range, the better.

According to Murray Ruggiero, 'If you don’t like the neighbouring numbers, you’ve got a
problem, because odds are, you will wind up with the results of
the neighbouring set of parameters.'

## Strategy Analysis
<img width="1026" height="470" alt="image" src="https://github.com/user-attachments/assets/6f97ccf4-6ce5-4784-8bce-a6522a418969" />

The sma crossover strategy produces some positive result on the GOOGLE stock. Indexes close to zero are the initial fast sma values starting from 1, and slow sma values starting from 10. the lookback period alternates between 10 and 20 for the sake of simplicity.

With the net profit getting better with increasing index value, it indicates that the strategy works better with higher fast sma values and higher slow sma values.

<img width="1026" height="470" alt="image" src="https://github.com/user-attachments/assets/48bf7349-acb9-40c7-bac6-f3bce6807b00" />

The goal of optimised strategies is to produce parameters with the best results and whose neighboring values produce similar results. This helps to ensure that in the case of chaning market conditions, the strategy can still produce positive results. The closest to this is the sma values within the index range 583 to 590.

<img width="1737" height="580" alt="image" src="https://github.com/user-attachments/assets/b8c2e3c4-7212-4301-9124-7f80e53ecadf" />


Starting from index 584 until 590, the strategy produced results in this order; £1559.47, £1077.51, £1141.02, -£102.74, £2329.85, £374.29, £242.56. For these ones the sma values for fast and slow are within the range 16 & 17 for fast sma and 18,19,20 for slow sma, while the lookback period alternates between 10 and 20. Unfortunately, this isn't the perfect scenario, but somewhat close. So we choose the parameter values as follows:

fast sma value = 17

slow sma value = 20

lookback value = 10

## The Result
<img width="1907" height="907" alt="image" src="https://github.com/user-attachments/assets/70a975d0-9ecb-4627-bf66-1623808f691e" />
<img width="1917" height="900" alt="image" src="https://github.com/user-attachments/assets/4b096c18-f9d2-494e-b906-eed3684d6334" />
<img width="1453" height="885" alt="image" src="https://github.com/user-attachments/assets/61543e01-6162-4610-ae73-62d68f05a222" />



