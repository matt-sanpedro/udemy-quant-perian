import pandas as pd
import numpy as np
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
df_fin = df_fin.set_index('Symbol',verify_integrity=True)
print('First 5 rows df_fin:\n{}'.format(df_fin.head(5)))

# Task: What are the 10 largest companies according to market cap?**
print('\nNLARGEST\nData type: {}\nData:\n{}'.format(type(df_fin['Market Cap'].nlargest(10)), df_fin['Market Cap'].nlargest(10)))

# Task: Return all information about the 10 largest companies according by market cap**
print('\n10 largest companies according to market cap:\n{}'.format(df_fin.nlargest(10,'Market Cap')))

# Task: Drop GOOG**
df_fin = df_fin.drop('GOOG')
print('\nDropped "GOOG" from df_fin:\n{}'.format(df_fin.nlargest(10,'Market Cap')))

# Task: How many companies have a dividend yield > 4% ?**
print('Number of companies with Dividend yield > 4%: {}'.format(len(df_fin[df_fin['Dividend Yield'] > 4])))

# Task: What is the mean Earnings per Share for all companies with a market cap > 1e+11**
print('Mean earnings per share for market cap > 1e11: {}'.format(df_fin[df_fin['Market Cap'] > 1e11]['Earnings/Share'].mean()))

# Task: How many companies have a positive earnings per shares ratio?**
print('Number of companies with positive earning per shares ratio: {}'.format(len(df_fin[df_fin['Earnings/Share'] > 0].sort_values('Earnings/Share'))))

# Task: Which company pays the highest dividend yield? What was its 52 week high?**
div_max_idx = df_fin['Dividend Yield'].idxmax()
print('Company with highest dividend yield: {}'.format(div_max_idx))
print('{} 52 week high is: {}'.format(div_max_idx, df_fin.loc[div_max_idx]['52 Week High']))

# Task: Return the company with the largest spread between 52 weeks high and low**
diff_52 = (df_fin['52 Week High'] - df_fin['52 Week Low']).abs()
print('Company with largest spread between 52 weeks high and low: {}'.format(diff_52.idxmax()))

# Task: Return all companies whith a price between \\$ 50 and \\$ 100**
print('Companies with share price between 50 and 100:\n{}'.format(df_fin[(df_fin['Price']>=50) & (df_fin['Price']<=100)].sort_values('Price')))

# Task: The market cap is really hard to read. Create a new column called "Market Cap in Billion" which shows the market cap in billions**
df_fin['Market Cap in Billion'] = df_fin['Market Cap'] / 1_000_000_000
print('New column:\n{}'.format(df_fin[['Price', 'Market Cap', 'Market Cap in Billion']]))

# Task: Is there a correlation between the market cap and the Dividend Yield?**
mcap_div_corr = df_fin['Market Cap'].corr(df_fin['Dividend Yield'])
print('Correlation between "Market Cap" and "Dividend Yield": {}'.format(mcap_div_corr))
print(df_fin.corr())

# Task: Merge the financials dataframe with the constituents dataframe**
df = pd.merge(left=df_cons,right=df_fin,how='outer',on='Symbol')
print('Symbol row duplicates exist: {}'.format(check_duplicates(df, 'Symbol')))
df = df.set_index('Symbol',verify_integrity=True)
print('Merged outer df:\n{}'.format(df))

# Task: Print all sectors. How often does each sector occur?**
print('Unique Sectors:\n{}'.format(df['Sector'].unique()))
print('Occurrences of Sectors:\n{}'.format(df['Sector'].value_counts()))

# Task: Replace Information Technology by "IT"**
print('Before "IT" replacement:\n{}'.format(df.loc[df['Sector'] == 'Information Technology']))
df['Sector'] = df['Sector'].replace('Information Technology', 'IT')
print('After "IT" replacement:\n{}'.format(df.loc[df['Sector'] == 'IT']))

# Task: Add a \$ before the stock price** f"${price:.2f}"
def add_dollar_sign(price):
    return f'${price:.2f}'
print('Before adding dollar sign:\n{}'.format(df))
# df['Price'] = np.vectorize(add_dollar_sign)(df['Price'])
df["Price"] = df["Price"].map("${:.2f}".format)
print('After adding dollar sign:\n{}'.format(df))
