import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df.describe())

# sort values: float
print(df.sort_values('tip'))

# sort values: string
print(df.sort_values('Payer Name', ascending=False))

# can sort by multiple columns
print(df.sort_values(['tip', 'size']))

# max value
print('Max value:    {}'.format(df['total_bill'].max()))

# index of max value
print('Index of max: {}'.format(df['total_bill'].idxmax()))

# min value
print('Min value:    {}'.format(df['total_bill'].min()))

# index of min value
print('Index of min: {}'.format(df['total_bill'].idxmin()))

# verify max index with iloc
row_idx = 170
print('The row index of {} has a series of:\n{}'.format(row_idx, df.iloc[row_idx]))

# correlation between column values for numeric values (Pearson correlation coefficient)
# NO correlation values will be closer to zero
print(df.corr(numeric_only=True))

# value counts for categorical columns
print('Sex counts:\n{}'.format(df['sex'].value_counts()))

# extract unique values from column
print('Number of unique values: {}\nUnique days: {}'.format(df['day'].nunique(), df['day'].unique()))

# replace single value
df['sex'] = df['sex'].replace(['Female', 'Male'], ['F', 'M'])

print('Changed sex col word to letter:\n{}'.format(df.head(5)))

# map function
mymap = {'F': 'Female', 'M': 'Male'}
df['sex'] = df['sex'].map(mymap)
print('Changed sex col letter to word:\n{}'.format(df.head(5)))

# duplicated method marks first occurrences as False
simple_df = pd.DataFrame([1,2,2,2,1], ['a','b','c','d','e'])
print(simple_df.duplicated())

# drop duplicates
print(simple_df.drop_duplicates())

# between method for numeric columns
print(df[df['total_bill'].between(10,20,inclusive='both')])

# nlargest with the tip column
print('\nNLARGEST\nData type: {}\nData:\n{}'.format(type(df['tip'].nlargest(10)), df['tip'].nlargest(10)))
print('Data type: {}\nData:\n{}'.format(type(df.nlargest(10, 'tip')), df.nlargest(10, 'tip')))

# nsmallest with the tip column
print('\nNSMALLEST\nData type: {}\nData:\n{}'.format(type(df['tip'].nsmallest(10)), df['tip'].nsmallest(10)))
print('Data type: {}\nData:\n{}'.format(type(df.nsmallest(10, 'tip')), df.nsmallest(10, 'tip')))

# take random sample from a dataframe
print('\nFive random sample rows:\n{}'.format(df.sample(5)))

# sample 10% random rows of the dataframe
print('\nSample 10 percent rows:\n{}'.format(df.sample(frac=0.1)))
