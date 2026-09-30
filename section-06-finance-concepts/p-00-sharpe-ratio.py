import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
# from matplotlib import dates

# resolve multiple csv paths
csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "DATA"))
csv_files = [
    "AAPL.csv",
    "COST.csv",
]

def compute_sharpe_ratio(df, risk_free_return=0):
    mean_return = df['Daily Return'].mean()
    std = df['Daily Return'].std()
    sharpe_ratio = (mean_return - risk_free_return) / std
    return sharpe_ratio * (252**0.5) 

frames = []
for csv_file in csv_files:
    csv_path = os.path.join(csv_dir, csv_file)
    df = pd.read_csv(csv_path, index_col='Date', parse_dates=True)
    frames.append(df)

for i, df in enumerate(frames, start=1):
    print(f'File {i}: {csv_files[i - 1]}')
    print(df.head())

# print('\nAAPL: {}'.format(frames[0]))
# print('\nCOST: {}'.format(frames[1]))

# compute daily returns
for i, df in enumerate(frames):
    df['Daily Return'] = df['Adj Close'].pct_change(1)
    # Drop only rows where the new Daily Return is missing.
    # A single call is enough; `dropna()` on the whole frame is broader than needed.
    frames[i] = df.dropna(subset=['Daily Return']).copy()
    sharp_ratio_annual = compute_sharpe_ratio(frames[i])
    print(f'{csv_files[i]} - Sharpe Ratio: {sharp_ratio_annual}')


print('\nAAPL Daily Return: {}'.format(frames[0]['Daily Return']))
print('\nCOST Daily Return: {}'.format(frames[1]['Daily Return']))
