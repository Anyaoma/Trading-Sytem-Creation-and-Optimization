## Net gain: Calculation after adding Commission and Slippage

#### figure 2.0: Result (Equity Curve) of the trading system with added commission and slippage cost
<img width="1917" height="922" alt="image" src="https://github.com/user-attachments/assets/daa8a7cc-837c-4b2c-b2d6-618c614386d0" />


#### figure 2.1: Underwater drawdown curve of the Trading system with added commission and slippage cost.
<img width="1918" height="788" alt="image" src="https://github.com/user-attachments/assets/46f5a2b9-f41b-49c0-ac60-5172d7483358" />


On average, the cost of commission is £5, and that of slippage is £4(three pips per stock) per round turn, which, when applied and accounted for within the trading system, results in a negative average trade net profit of -£0.91 as identified in fig.2.3.

## Before Commission and Slippage:
#### figure 2.2: Trading system metrics before commission and slippage cost
<img width="1485" height="922" alt="image" src="https://github.com/user-attachments/assets/0799657e-7a09-40fb-ad67-6bb1148dec0f" />


## After Commission and Slippage:

#### figure 2.3: Trading system metrics after commission and slippage cost
<img width="1452" height="917" alt="image" src="https://github.com/user-attachments/assets/97a05736-c285-4c41-a20f-11e3c48f99d4" />


The detailed equity curve and drawdown graph in fig.2.0 and fig.2.1 show the result of a more realistic application of the trading system. The equity curve shows more oscillations than before, and the maximum drawdown is up to 2.68% of the account balance, higher than the previous 2.38% when commission and slippage costs weren't yet added.

The result of this trading system seems to be very underwhelming. In the current state of the system, one is far from being profitable on the Google stock. However, it could be that the arbitrarily chosen parameters of the system (fast sma, slow sma, and lookback values) might not be a good fit; they could be suitable or not. So the key question to answer is; is this trading system useless overall, or does it just suffer from poor parameter inputs. To answer this question, we perform more system test like the ones shown in section 1(01_Initial_Trade_Strategy)  will be performed for different input parameters. This will be performed in the next section (03_Variation of Input Parameters), where I also detail specifics to look out for and pitfalls to avoid.


