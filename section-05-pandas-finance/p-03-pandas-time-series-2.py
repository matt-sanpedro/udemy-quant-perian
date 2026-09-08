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

plt.figure(figsize=(8,6),dpi=200)
ax = df['Close']['2018-01-01':'2020-01-01'].plot()
ax.xaxis.set_major_locator(dates.YearLocator())
ax.xaxis.set_major_formatter(dates.DateFormatter('%Y      %B'))
ax.xaxis.set_minor_locator(dates.MonthLocator())
ax.xaxis.set_minor_formatter(dates.DateFormatter('%B'))
ax.tick_params(axis='x',which='minor',rotation=90)
ax.tick_params(axis='x',which='major',rotation=90)
plt.xticks(ha='center')
ax.grid(True,axis='both',which='both')
ax.set_title('Costco: Closing Price')
plt.tight_layout()
plt.show()
