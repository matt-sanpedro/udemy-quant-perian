import pandas as pd
import matplotlib.pyplot as plt
import os

# resolve the csv path
csv_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "DATA", "COST.csv")
)
df = pd.read_csv(csv_path)
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date',verify_integrity=True)
print(df.index)
df['Adj Close'].plot()
plt.show()
