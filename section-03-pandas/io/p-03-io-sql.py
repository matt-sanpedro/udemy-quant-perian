import pandas as pd
import numpy as np
from sqlalchemy import create_engine

"""
Pandas SQL
    - can write to various SQL engines through driver and sqlalchemy python library
    - industry engines include: PostgreSQL, MySQL, MS SQL Server
    - will use SQLite for example, which creates temporary database in RAM

Determine SQL engine and Python library setup
    1. PostgreSQL:      psycopg2
    2. MySQL:           pymysql
    3. MS SQL Server:   pyodbc

Use sqlalchemy library to connect SQL database with driver
    - sqlalchemy driver runs with pandas read_sql method
    - pandas can read entire tables OR parse a SQL query
"""

# create temp db and write SQL
temp_db = create_engine('sqlite:///:memory:')
np_arr = np.random.randint(low=0,high=100,size=(4,4))
print('Numpy array:\n{}'.format(np_arr))
df = pd.DataFrame(data=np_arr, columns=['a','b','c','d'])
print('DataFrame object:\n{}'.format(df))
df.to_sql(name='new_table', con=temp_db, index=False)

# 1. Read SQL by read_sql method
new_df = pd.read_sql(sql='new_table',con=temp_db)
print('Read DataFrame object:\n{}'.format(new_df))

# 2. Read SQL by SELECT statement
sel_df = pd.read_sql_query(sql='SELECT a,c FROM new_table', con=temp_db)
print('SQL Query DataFrame object:\n{}'.format(sel_df))
