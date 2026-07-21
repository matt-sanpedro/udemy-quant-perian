import numpy as np
import pandas as pd
import os

"""
dataframe: a group of pandas series objects that share the same index
    - technically, it is a two-dimensional (size-mutable) tabular data structure
    - contains labeled axes (rows and columns)
"""

# create a dataframe from Python objects
np.random.seed(101)
# note that the high number is exclusive
mydata = np.random.randint(0, 101, (4,3))
print(mydata)

myindex = ['CA', 'NY', 'AZ', 'TX']
mycolumns = ['Jan', 'Feb', 'Mar']
df = pd.DataFrame(data=mydata, index=myindex, columns=mycolumns)
print(df)

# info method
df.info()

# read the csv file
# robust way to read files: prevents issues with path separators
df_csv = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df_csv)
