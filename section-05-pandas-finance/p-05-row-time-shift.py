import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
# from matplotlib import dates

# resolve the csv path
csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "DATA", "WMT.csv")
)
df = pd.read_csv(csv_path,index_col='Date',parse_dates=True)
print('DATAFRAME (no shift):\n{}'.format(df))
# df.info()

'''
time shifting with dataframe rows will be used for calculating 
percent change or capital asset pricing model

shift 1: first row is NaN, last row data is lost
shift -1: last row is NaN, first row data is lost
'''
print('Shift (1):\n{}'.format(df.shift(1)))
print('Shift (-1):\n{}'.format(df.shift(-1)))

# can also shift by larger periods of time
print('Shift (1 month):\n{}'.format(df.shift(periods=1,freq='M')))

# what is the time difference from the previous day
print(df['Adj Close'].diff(1))
fig = plt.figure(figsize=(8,10),dpi=200)
# df['Adj Close'].diff(1).plot()

# what is the time difference (in percent) from the previous day
df['Adj Close'].pct_change(1).plot()
plt.show()

# cumulative sum or product
example_series = pd.Series(np.arange(1,5))
example_series_np = np.arange(1,5)
print(type(example_series))
print(type(example_series_np))

print('pandas series:\n{}'.format(example_series))
print('cumulative sum:\n{}'.format(example_series.cumsum()))
print('cumulative product:\n{}'.format(example_series.cumprod()))
