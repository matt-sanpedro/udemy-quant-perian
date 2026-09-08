import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import dates

# resolve the csv path
csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "DATA", "WMT.csv")
)
df = pd.read_csv(csv_path,index_col='Date',parse_dates=True)
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.set_index('Date',verify_integrity=True)

# ADJ CLOSE AND MA PLOT
plt.figure(figsize=(10,4),dpi=200)
ax = df['Adj Close'].plot(label='Adj Close')
df['Adj Close'].rolling(window=100).mean().plot(lw=0.8,label='100 MA')
df['Adj Close'].rolling(window=200).mean().plot(lw=0.8,label='200 MA')
ax.legend()
ax.set_title('Walmart: Adj Close and Moving Average')
# ax.xaxis.set_major_locator(dates.YearLocator())
# ax.xaxis.set_major_formatter(dates.DateFormatter('%Y      %B'))
# ax.xaxis.set_minor_locator(dates.MonthLocator())
# ax.xaxis.set_minor_formatter(dates.DateFormatter('%B'))
# ax.tick_params(axis='x',which='minor',rotation=90)
# ax.tick_params(axis='x',which='major',rotation=90)
# plt.xticks(ha='center')
# ax.grid(True,axis='both',which='both')
plt.tight_layout()
plt.show()

# STANDARD DEVIATION PLOT
plt.figure(figsize=(8,3),dpi=200)
ax1 = df['Adj Close'].rolling(window=5).std().plot(lw=0.8,label='5 Day')
df['Adj Close'].rolling(window=10).std().plot(lw=0.8,label='10 Day')
df['Adj Close'].rolling(window=20).std().plot(lw=0.8,label='20 Day')
ax1.legend(loc='upper left')
ax1.set_title('Walmart: Standard Deviation for Volatility')
plt.tight_layout()
plt.show()
