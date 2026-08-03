import pandas as pd
import os

# conditional filtering: select rows based on a condition on a column

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# filter for payments over $40 -> outputs a series of boolean values
print(df[df['total_bill'] > 40])
print(df[df['sex'] == 'Female'])

# AND & --- both conditions need to be true
# OR  | --- either condition is true
print(df[(df['total_bill'] > 30) & (df['sex'] == 'Male')])

# filtering the weekend days
print(df[(df['day'] == 'Sat') | (df['day'] == 'Sun')])

# for filtering on same column, can use a shortcut with "is in" method
options = ['Sat', 'Sun']
print(df[df['day'].isin(options)])
