import pandas as pd
import numpy as np

"""
concatenation: in Pandas, act of pasting two DataFrames together by columns or rows
    - Pandas automatically fills in NaN where necessary
"""
data_one = {'A': ['A0', 'A1', 'A2', 'A3'], 'B': ['B0', 'B1', 'B2', 'B3']}
data_two = {'C': ['C0', 'C1', 'C2', 'C3'], 'D': ['D0', 'D1', 'D2', 'D3']}
one = pd.DataFrame(data_one)
two = pd.DataFrame(data_two)

df = pd.concat([one, two], axis=1)
print('concat by columns:\n{}'.format(df))

# concat by row
two.columns = one.columns
df = pd.concat([one, two])
# reset the indices
df.index = range(len(df))
print('\nconcat by rows:\n{}'.format(df))
