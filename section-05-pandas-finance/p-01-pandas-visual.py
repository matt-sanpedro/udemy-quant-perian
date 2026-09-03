import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__),'SPY2000_2021.csv'))
print(df)

# line plot by default
# df[['Adj Close', 'High']].plot()

# histogram 
# df['Volume'].plot(kind='hist',bins=100)

# histogram smooth curve versionn
# df['Volume'].plot(kind='kde')

# SOLUTION 1: can connect matplotlib figure object to the pandas object
plt.figure(figsize=(10,3),dpi=200)
# df['Volume'].plot(kind='line',c='red')
ax = df['Adj Close'].plot(lw=1,label='Adjusted Close')
df[['Low','High']].plot(ls='--',lw=0.8,ax=ax)
plt.legend(loc='best')
plt.show()

# SOLUTION 2: can use the subplots feature from matplotlib
fig,ax1 = plt.subplots()
df['Adj Close'].plot(lw=1,ax=ax1,xlabel='X axis')
df[['Low','High']].plot(ls='--',lw=0.8,ax=ax1)
plt.legend(loc='best')
# plt.xlabel('X axis')
plt.show()
