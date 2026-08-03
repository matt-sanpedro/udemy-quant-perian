import numpy as np
import pandas as pd
import os

# read the csv file
df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
print(df.index)

# # duplicate location
# print(df.iat[118, 10])
# print(df.iat[205, 10])

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
        Duplicate or NaN values exists
    False:
        All values in the column have no duplicates or NaN values
    """
    has_dup = df[df[index_col].duplicated()].shape[0] > 0
    has_nan = df[index_col].isna().any().any()
    return has_dup or has_nan

def gen_unique_index(df: pd.DataFrame, index_col: str):
    """
    Generates a custom index if duplicates are found

    Parameters
    ----------
    df : pd.DataFrame
        The source DataFrame to inspect.
    index_col : str
        The column name intended to become the future index.

    Returns
    -------
    df : pd.DataFrame
        The DataFrame with the "index_col" with all unique values 
    """
    has_dup = df[df[index_col].duplicated()].shape[0] > 0
    if has_dup:
        col_position = df.columns.get_loc(index_col)
        print('Column position: {}'.format(col_position))
        duplicate_rows = df[df[index_col].duplicated(keep=False)]
        # print('Duplicate rows found:\n{}'.format((duplicate_rows['Payment ID'].index)))
        # duplicate_rows[index_col] = duplicate_rows[index_col]
        for i in range(duplicate_rows.shape[0]):
            # print(i)
            row_position = duplicate_rows['Payment ID'].index[i]
            print(row_position)
            print(duplicate_rows['Payment ID'][row_position])
            # duplicate_rows['Payment ID'][i] = duplicate_rows['Payment ID'][duplicate_rows['Payment ID'].index[i]] + str(duplicate_rows['Payment ID'].index[i])
            df.iat[row_position, col_position] = duplicate_rows['Payment ID'][row_position] + str(row_position)
            print(df.iat[row_position, col_position])

    return df

print('Check Duplicate: {}'.format(check_duplicates(df, index_col)))

# invoke the gen_unique_index function
unique_df = gen_unique_index(df, index_col)
print('Check Duplicate: {}'.format(check_duplicates(unique_df, index_col)))
print(unique_df)

# set index
unique_df = unique_df.set_index(index_col)
print(unique_df)
