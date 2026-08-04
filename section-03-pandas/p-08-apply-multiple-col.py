import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

# simple function
def simple(num):
    return num*2

# lambda function
lambda num: num*2

# can use apply with lambda functions
print('apply with lambda:\n{}'.format(df['total_bill'].apply(lambda num: num*2)))

# calculate the tip quality
def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return 'Generous'
    else:
        return 'Other'

# apply the quality function
df['quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)
print('Apply method:\n{}'.format(df[['total_bill', 'tip', 'quality']].tail(15)))

# np.vectorize for faster computational time and simpler syntax
df['quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
print('np.vectorize method:\n{}'.format(df[['total_bill', 'tip', 'quality']].tail(15)))
