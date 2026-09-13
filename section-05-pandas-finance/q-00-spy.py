import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib import dates

csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "SPY2000_2021.csv")
)
df = pd.read_csv(csv_path,index_col='Date',parse_dates=True)
# print(df.index)

# **Task: Check the head of the ten first entries in the dataset**
print(df.head(10))

# **Task: Check the datatype of all entries**
df.info()

# **Task: Plot the Adjusted Closing price of the SP500, with the price on the y axis and the year on the x axis. Use Locator() and Formatter() techniques to configure the plot x axis so that you can see a tick for every year in the dataset (only showing the year number, not the full YYYY-MM-DD that is the default). Choose a reasonable figure size, set the dpi to 300 and save this plot in your working directory as sp500.png**
plt.figure(figsize=(10,6),dpi=300)
ax = df['Adj Close'].plot()
ax.xaxis.set_major_locator(dates.YearLocator())
ax.tick_params(axis='x',which='major',rotation=90)
plt.xticks(ha='center')
plt.tight_layout()
plt.savefig('sp500.png',bbox_inches='tight')
# plt.show()

# **Task: Create a histogram of the daily volume of shares of SPY traded. Choose a reasonable bin size.**
df['Volume'].plot(kind='hist',bins=50)
# plt.show()

# **Task: Let's explore the crash and recovery of 2020 due to the COVID pandemic. Create a line plot of the Adj. Close price from 1-1-2020 to 1-1-2021. The xaxis ticks should be formatted by YYYY-MM**
plt.figure(figsize=(8,6),dpi=200)
df['Adj Close'].plot(xlim=['2020-01-01','2021-01-01'])
# plt.show()

# **Task: Create a plot whichs shows the adjusted closing price of SPY for the entire length of the time series along with an added trend line of the corresponding 200 days rolling mean of the adj. close price. Make sure to add a legend that identifies each line.** 
plt.figure(figsize=(10,4),dpi=200)
ax_adj = df['Adj Close'].plot(label='Adj Close')
df['Adj Close'].rolling(window=200).mean().plot(lw=0.8,label='200 MA of Adj Close')
ax_adj.legend()
# plt.show()

'''
**Task: If you bought one share at the start of the time series on Jan 1st 2000, how much money would you have gained (in Adj. Close Dollar amount) by Jan 1st 2021?**

Take the adjusted closing price as reference
'''
gains = df['Adj Close']['2020-12-31'] - df['Adj Close']['2000-01-03']
print('Gains from one share of SPY: {}'.format(gains))

# **Task: What was the percent increase in value (based on Adj. Close price) from Jan 1st, 2000 to Jan 1st 2021?**
percent_inc = gains/df['Adj Close']['2000-01-03'] * 100
print('Percent increase from one share of SPY: {}'.format(percent_inc))

# **Task: Return the 10 dates with the largest gain for the SPY.**
df['Delta Adj Close'] = df['Adj Close'].pct_change(1)
print('Largest gain for the SPY: {}'.format(df['Delta Adj Close'].nlargest(10))) 

# **TASK: What were the 10 dates with the highest daily percent change from the previous day (either gain OR decrease).**
print(df['Delta Adj Close'].abs().nlargest(10))

# **Task: For each year in the dataset, find the Maximum Adj. Close price that SPY reached for that year.**
annual_max = df['Adj Close'].resample('YE').max()
print('Max Adj Close of SPY per year:\n{}'.format(annual_max))

'''
**Task: What was the day with the lowest adjusted closing price in 2020? (and what was this price)** 

Hint: Check out idxmin()
'''
# print('Price of lowest adjusted closing: {}'.format(df['Adj Close']['2020-01-01':'2020-12-31'].min()))
print('Price of lowest adjusted closing: {}'.format(df.loc['2020-01-01':'2020-12-31', 'Adj Close'].min()))
# print('Day with lowest adjusted closing: {}'.format(df['Adj Close']['2020-01-01':'2020-12-31'].idxmin()))
print('Day with lowest adjusted closing: {}'.format(df.loc['2020-01-01':'2020-12-31', 'Adj Close'].idxmin()))

# **Task: In 2020, due to the uncertainty of the COVID-19 pandemic, the S&P500 index experienced a large drop in March of 2020. What was the highest price reached in 2020 *before* April 1st, 2020.**
# high_index = df['Adj Close']['2020-01-01':'2020-03-31'].idxmax()
high_index_eff = df.loc['2020-01-01':'2020-03-31', 'Adj Close'].idxmax()
# high_price = df['Adj Close']['2020-01-01':'2020-03-31'].max()
high_price_eff = df.loc['2020-01-01':'2020-03-31', 'Adj Close'].max()

print('Highest price of SPY before 2020-04-01: {}'.format(high_price_eff))
print('Timestamp: {}'.format(high_index_eff))
'''
**Task: Due to central bank and government actions, the S&P500 had one of the quickest recoveries in history after the crash of March 2020. How long did it take (in days) to reach the peak price the S&P 500 was at before the crash in March? In other words, based on your previous task of finding the peak price before the crash, how long did it take for the market to recover to its pre-crash price level?**

Hint: You can subtract datetime timestamps from each other

Learn: Consider using the .loc method for an efficient calculation
    - Avoids Chained Indexing: Your original code slices the series (['2020-04-01':'2020-12-31']) and then filters it with a boolean mask built from the entire series (df['Adj Close'] > high_price). While pandas handles this, mixing sizes like this can cause unexpected errors or performance warnings. .loc filters everything at once safely.

    - Performance: Using .gt() (greater than) and .idxmax() reads like a sentence and executes efficiently in __vectorized__ pandas operations (SEE: section-03-pandas/p-09-timeit.py).
'''
# recover_price = df['Adj Close']['2020-04-01':'2020-12-31'][df['Adj Close'] > high_price].index[0]
recover_price = df.loc['2020-04-01':'2020-12-31', 'Adj Close'].gt(high_price_eff).idxmax()
print('Time Delta for SPY recovery: {}'.format(recover_price - high_index_eff))
