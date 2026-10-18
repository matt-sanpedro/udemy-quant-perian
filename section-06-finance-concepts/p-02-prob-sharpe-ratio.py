'''
Probabilistic Sharpe Ratio (PSR): 
    - probability that the estimated Sharpe Ratio is greater than a chosen benchmark
    - enables reporting example of: 95% chance of SR of 1.6
    - in 2000, "The Sharpe Ratio Efficient Frontier" (David Bailey and Marcos Lopes de Prado)
    - analyzes the Sharpe Ratio with skew and kurtosis measurements
    - calculates Sharpe Ratio in probabistic terms 

Kurtosis: measurement in financial analysis to gauge an investment's risk of price volatility
    - measures distribution tails relative to the center
    - three types: 
        1. mesokurtic: normal
        2. leptokurtic: high risk
        3. platykurtic: low risk
    - accesses tail risk, or risk of extreme price swings in investments
    - positive excess kurtosis suggests high risk (possible large gains/losses)

Skewness: measure of asymmetry of the probabistic distribution

Use cases:
    - conduct/design trading algorithms on QuantConnect
    - evaluate performance

Resources:
    - Excel calculation example: https://www.youtube.com/watch?v=yKPNjru2Ry4
'''
