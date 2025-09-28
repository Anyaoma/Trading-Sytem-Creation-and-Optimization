## Variation of the input parameters: optimisation and stability diagrams

Every trading system is in some form an optimization; in choosing any trading system one must have compared it to some others, and proceed to choose it because it shows favorable and predictive results. So the key question is: which set of parameter values works best for the trading system backtest and produces profits in the future in real trading? While the answer to this question is different for every trading system, the one rule that applies to all is that: the neighbourhood or surrounding values of the chosen parameter values must be nearly as profitable as the chosen system parameters, and the bigger this profitable parameter range, the better.

According to Murray Ruggiero, 'If you don’t like the neighbouring numbers, you’ve got a
problem, because odds are, you will wind up with the results of
the neighbouring set of parameters.'

# Strategy Analysis
<img width="1026" height="470" alt="image" src="https://github.com/user-attachments/assets/6f97ccf4-6ce5-4784-8bce-a6522a418969" />

The sma crossover strategy produces some positive result on the GOOGLE stock. Indexes close to zero are the initial fast sma values starting from 1, and slow sma values starting from 10. the lookback period alternates between 10 and 20 for the sake of simplicity.

With the net profit getting better with increasing index value, it indicates that the strategy works better with higher fast sma values and higher slow sma values.
