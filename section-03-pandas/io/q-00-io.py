import pandas as pd
import os

def get_col_datatype(df):
    col_dict = {}
    for col in df.columns:
        col_dict[col] = df[col].dtype
    return col_dict

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
