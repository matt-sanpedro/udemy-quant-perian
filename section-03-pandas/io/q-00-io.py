import pandas as pd
import os

def get_col_datatype(df):
    col_dict = {}
    for col in df.columns:
        col_dict[col] = df[col].dtype
    return col_dict

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

# Read the two datasets provided in the current directory (also available in the DATA folder. 
# (The file names are: constituents.csv and constituents-financials.csv)
df_cons = pd.read_csv(os.path.join(os.path.dirname(__file__), 'constituents.csv'))
df_fin = pd.read_csv(os.path.join(os.path.dirname(__file__), 'constituents-financials.csv'))
# print('constituents:\n{}'.format(df_cons))
# print('constituents COLUMNS:\n{}'.format(df_cons.columns))
# print('constituents INFO:')
# df_cons.info()

# print('\nconstituents financials:\n{}'.format(df_fin))
# print('constituents financials COLUMNS:\n{}'.format(df_fin.columns))
# print('constituents financials INFO:')
# df_fin.info()

# List all columns of the two datasets. Additionally retrieve the datatype for each column**
print(get_col_datatype(df_cons))
print(get_col_datatype(df_fin))
print(df_cons.dtypes)
print(df_fin.dtypes)

# Print the first 5 rows of both datasets**
print('First 5 rows df_cons:\n{}'.format(df_cons.head(5)))
print('First 5 rows df_fin:\n{}'.format(df_fin.head(5)))

# Task: Drop the SEC Filings column**
df_fin = df_fin.drop('SEC Filings',axis=1)
print('First 5 rows df_fin:\n{}'.format(df_fin.head(5)))

# Task: Set the Symbol column to the index in the financials dataset**
print('Symbol row duplicates exist: {}'.format(check_duplicates(df_fin, 'Symbol')))
df_fin = df_fin.set_index('Symbol')
print('First 5 rows df_fin:\n{}'.format(df_fin.head(5)))

# Task: What are the 10 largest companies according to market cap?**
print('\nNLARGEST\nData type: {}\nData:\n{}'.format(type(df_fin['Market Cap'].nlargest(10)), df_fin['Market Cap'].nlargest(10)))

# Task: Return all information about the 10 largest companies according by market cap**
print('\n10 largest companies according to market cap:\n{}'.format(df_fin.nlargest(10,'Market Cap')))
