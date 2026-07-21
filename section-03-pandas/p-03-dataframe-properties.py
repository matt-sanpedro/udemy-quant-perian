import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# list the columns in a dataframe
print(df.columns)

# returns boolean if column exists in df
print('total_bill' in df.columns)

# can loop through the columns
for col in df.columns:
    print(col)

# extract indices
print(df.index)

# print first couple of rows
print(df.head(10))

# print last couple of rows
print(df.tail(20))

# get the df info
df.info()

# for numeric columns, calculate statistics
print(df.describe())

# can also call transpose on the describe method
print(df.describe().transpose())
