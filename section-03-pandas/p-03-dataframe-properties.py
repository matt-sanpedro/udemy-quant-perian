import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# list the columns in a dataframe
print('Calling columns method to list the columns: {}'.format(df.columns))

# returns boolean if column exists in df
print('total_bill' in df.columns)

# can loop through the columns
for col in df.columns:
    print(col)

# extract indices
print('Calling index method to list the indices: {}'.format(df.index))

# print first couple of rows
print(df.head(3))

# print last couple of rows
print(df.tail(5))

# get the df info
print('\nInfo on DF:')
df.info()

# for numeric columns, calculate statistics
print('Calling the describe method:\n{}'.format(df.describe()))

# can also call transpose on the describe method
print('Transposing the describe statistics:\n{}'.format(df.describe().transpose()))
