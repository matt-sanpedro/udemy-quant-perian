import pandas as pd
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'example.csv'))
print('Read df:\n{}'.format(df))

# set the headers as a row with the header argument
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'example.csv'), header=None)
print('Read header=None:\n{}'.format(df))

# set the column "a" as the index
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'example.csv'), index_col=0)
print('Read index_col=0:\n{}'.format(df))

# saving with no index references
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'example.csv'))
df.to_csv('newfile.csv', index=False) # saves index by default
