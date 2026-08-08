import timeit

setup = '''
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return 'Generous'
    else:
        return 'Other'
'''

# apply the quality function
stmt_one = '''
df['quality'] = df[['total_bill', 'tip']].apply(lambda df: quality(df['total_bill'], df['tip']), axis=1)
'''

stmt_two = '''
df['quality'] = np.vectorize(quality)(df['total_bill'], df['tip'])
'''

print('Time apply method:   {} s'.format(round(timeit.timeit(setup=setup, stmt=stmt_one, number=1000), ndigits=6)))
print('Time np vect method: {} s'.format(round(timeit.timeit(setup=setup, stmt=stmt_two, number=1000), ndigits=6)))
