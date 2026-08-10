import pandas as pd
import os

"""
Pandas Read/Write Excel
    - can only read and write in raw data
    - cannot read macros, visualization, or formulas in spreadsheet
"""

# read specific sheet
table = pd.read_excel(os.path.join(os.path.dirname(__file__), 'my_excel_file.xlsx'), sheet_name='First_Sheet')
print('Read Excel:\n{}'.format(table))

# read entire sheet
tables = pd.ExcelFile(os.path.join(os.path.dirname(__file__), 'my_excel_file.xlsx'))
print('\nAvailable sheets: {}'.format(tables.sheet_names))

# read all the sheets into a dictionary
excel_dict = pd.read_excel(os.path.join(os.path.dirname(__file__), 'my_excel_file.xlsx'), sheet_name=None)
print('Read Excel:\n{}'.format(excel_dict))
print('Stores df:\n{}'.format(excel_dict['First_Sheet']))

# save to excel file
s_name = 'First_Sheet'
df = excel_dict[s_name]
df.to_excel(os.path.join(os.path.dirname(__file__), 'example_First_Sheet.xlsx'), sheet_name=s_name, index=False)
