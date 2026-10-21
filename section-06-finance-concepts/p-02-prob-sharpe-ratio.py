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
import scipy.stats
import os
import pandas as pd

def compute_sharpe_ratio(df, risk_free_return=0):
    mean_return = df['Daily Return'].mean()
    std = df['Daily Return'].std()

    # DAILY SHARPE RATIO
    return (mean_return - risk_free_return) / std

def compute_psr(df, benckmark=0):
    sr = compute_sharpe_ratio(df)
    skew = scipy.stats.skew(df['Daily Return'])
    kurtosis = scipy.stats.kurtosis(df['Daily Return'], fisher=True)
    n = len(df)

    sigma_sr = ( (1/(n-1)) * (1 + 0.5*sr**2 + skew*sr + (kurtosis/4)*sr**2) )**0.5
    ratio = (sr-benckmark)/sigma_sr
    psr = scipy.stats.norm.cdf(ratio)
    return psr

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "DATA", "AAPL.csv")
)
df = pd.read_csv(csv_path,index_col='Date',parse_dates=True)
df['Daily Return'] = df['Adj Close'].pct_change(1)
print(df)
df = df.dropna(subset=['Daily Return']).copy()
print(df)

psr_aapl = compute_psr(df)
print(psr_aapl)
