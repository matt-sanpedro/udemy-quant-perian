import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# extract panda series from the dataframe
print(df['total_bill'])
print(type(df['total_bill']))

# extract multiple columns
mycols = ['total_bill', 'tip']
print(df[mycols])
print(type(df[mycols]))

# addition operation between pandas series
print(df['total_bill'] + df['tip'])

# create a new tip percentage column
df['tip_percentage'] = np.round(100 * df['tip'] / df['total_bill'], 2)
print(df)

# referencing a column will overwrite 
df['price_per_person'] = np.round(df['total_bill'] / df['size'], 2)
print(df)

# removing columns with the drop method
# another option would be to use the inplace parameter but may deprecate soon 
df = df.drop('tip_percentage', axis=1)
print(df)

# the axis enumeration is related to the shape of numpy arrays
print(df.shape)
