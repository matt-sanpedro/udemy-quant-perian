import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# setting a new index, good practice to ensure all values are unique (Payment ID)
# identify the duplicate values
index_col = 'Payment ID'
print('All values in the {} column are unique: {}'.format(index_col, df[index_col].is_unique))
duplicates = df[df.duplicated()]
print('The duplicates in {} column are: {}'.format(index_col, duplicates))

df = df.set_index('Payment ID')
print(df)
