import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df)

"""
DUPLICATE CHECK
    - setting a new index, good practice to ensure all values are unique (Payment ID)
    - identify the duplicate values
"""
index_col = 'Payment ID'
print('All values in the {} column are unique: {}'.format(index_col, df[index_col].is_unique))
duplicates = df[df[index_col].duplicated()]
print('The duplicates in {} column are:\n{}'.format(index_col, duplicates))
has_dup = df[index_col].duplicated().any()
print('The duplicates in {} column are:\n{}'.format(index_col, has_dup))

# Returns True if ANY cell in the entire DataFrame is NaN
has_nan = df.isna().any().any()
print('NaN values exist: {}'.format(has_nan))

# Locate the duplicated values
duplicate_rows = df[df[index_col].duplicated(keep=False)]
print('Duplicate count:\n{}\nDuplicate values:\n{}'.format(len(duplicate_rows), duplicate_rows))

def check_duplicates(df: pd.DataFrame, index_col: str):
    """
    Determines if the given column has duplicate or NaN values
        
    Parameters
    ----------
    df : pd.DataFrame
        The source DataFrame to inspect.
    index_col : str
        The column name intended to become the future index.

    Returns
    -------
    True
        Duplicate or NaN values identified
    False:
        All values in the column have no duplicates or NaN values
    """
    has_dup = df[df[index_col].duplicated()].shape[0] > 0
    has_nan = df.isna().any().any()
    return has_dup and not has_nan

print('Check Duplicate: {}'.format(check_duplicates(df, index_col)))
