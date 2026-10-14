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

def compute_sortino_ratio(df, risk_free_return=0, threshold=0):
    '''
    VOLATILITY (THRESHOLD)
    T=0 --> NEGATIVE DAILY RETURNS

    Aspect	            | Chained Indexing (Your Original Code)	                        | .loc Method (Optimized Code)
    --------------------------------------------------------------------------------------------------------------------------------------------------------------
    Execution Steps	    | Two operations: First filters rows, then filters the column.	| One operation: Filters rows and selects the column simultaneously.
    Memory Performance	| Often creates a temporary intermediate copy in memory.	    | Operates directly on the existing DataFrame in-place.
    Safety Warning	    | Frequently triggers Pandas' SettingWithCopyWarning if you     | Safe. Guarantees modifications apply directly to the original DataFrame.
                        | try to modify the data later.	                                
    '''
    downside = df[df['Daily Return']<threshold]['Daily Return']
    downside_opt = df.loc[df['Daily Return'] < threshold, 'Daily Return']
    mean_return = df['Daily Return'].mean()
    print('DOWNSIDE:\n{}'.format(downside))
    print('DOWNSIDE OPTIMIZED:\n{}'.format(downside_opt))
    std = downside_opt.std()
    sortino_ratio = (mean_return - risk_free_return)/std
    return sortino_ratio * (252**0.5)

frames = []
for csv_file in csv_files:
    csv_path = os.path.join(csv_dir, csv_file)
    df = pd.read_csv(csv_path, index_col='Date', parse_dates=True)
    # df.info()
    frames.append(df)

'''
compute daily returns

Why .copy() is called
copy() makes a separate DataFrame object instead of reusing the same underlying data as df.

This matters because:

df is a local DataFrame created from the CSV.
They later do operations on it and then assign it into frames.
Without .copy(), pandas may return a view or keep overlapping references, which can cause confusing side effects if you modify one DataFrame and unexpectedly affect another.
In short, .copy() makes the cleaned version explicit and independent

This is safer and clearer than relying on pandas’ internal memory behavior.
'''
for i, df in enumerate(frames):
    df['Daily Return'] = df['Adj Close'].pct_change(1)
    # Drop only rows where the new Daily Return is missing.
    # A single call is enough; `dropna()` on the whole frame is broader than needed.
    frames[i] = df.dropna(subset=['Daily Return']).copy()
    print(f'File {i}: {csv_files[i]}')
    print('DAILY RETURN\n{}'.format(frames[i]['Daily Return']))
    print('ADJUSTED CLOSE\n{}'.format(frames[i]['Adj Close']))
    # sharpe_ratio_annual = compute_sharpe_ratio(frames[i])
    # print(f'{csv_files[i]} - Sharpe Ratio: {sharpe_ratio_annual}')
    sortino_ratio_annual = compute_sortino_ratio(frames[i])
    print(f'{csv_files[i]} - Sortino Ratio: {sortino_ratio_annual}')
