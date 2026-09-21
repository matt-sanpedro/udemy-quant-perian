import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import dates

# resolve the csv path
csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "DATA", "COST.csv")
)
df = pd.read_csv(csv_path)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date',verify_integrity=True)
print(df.index)

print(df['Adj Close']['2018-01-01':'2020-01-01'])

# SOLUTION 1: can slice a dataframe
df['Adj Close']['2018-01-01':'2020-01-01'].plot()
plt.show()

# SOLUTION 2: can call the xlim method
df['Adj Close'].plot(xlim=['2018-01-01','2020-01-01'],ylim=[150,300])
plt.show()

plt.figure(dpi=200)
ax = df['Close']['2018-01-01':'2018-03-01'].plot()
# ax.xaxis.set_major_locator(dates.WeekdayLocator(byweekday=0))

# LOCATORS: set axes location of the ticks to a particular date position
ax.xaxis.set_major_locator(dates.MonthLocator())
# FORMATTER: format actual time stamp to string
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y-%B'))
plt.tight_layout()
plt.show()
