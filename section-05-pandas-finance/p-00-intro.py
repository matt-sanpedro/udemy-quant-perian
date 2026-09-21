import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

from datetime import datetime

myyear = 2015
mymonth = 1
myday = 1
myhour = 2
mymin = 30
mysec = 15

mydate = datetime(myyear,mymonth,myday)
print('Time: {}\nType: {}'.format(mydate, type(mydate)))

mydatetime = datetime(myyear,mymonth,myday,myhour,mymin,mysec)
print('Time: {}\nType: {}'.format(mydatetime, type(mydatetime)))

# can call attributes
print('Year: {}'.format(mydatetime.year))

# datetime and pandas
myser = pd.Series(['Nov 3, 1990', '2000-01-01', None])
timser = pd.to_datetime(myser,format='mixed')

# euro date conversion
obvi_euro_date = '31-12-2000'
print(pd.to_datetime(obvi_euro_date))

euro_date = '10-12-2000'
print(pd.to_datetime(euro_date,dayfirst=True))

# formatting different dates
style_date = '12--Dec--2000'
print(pd.to_datetime(style_date,format='%d--%b--%Y'))

custom_date = '11th of Dec 2000'
print(pd.to_datetime(custom_date))

# reading in time data
df_csv = pd.read_csv(os.path.join(os.path.dirname(__file__), 'SPY2000_2021.csv'))
print(df_csv['Date'])
# print(df_csv)

df_csv['Date'] = pd.to_datetime(df_csv['Date'])
print(df_csv['Date'])

# parse the date while reading csv
df_date_parse = pd.read_csv(os.path.join(os.path.dirname(__file__), 'SPY2000_2021.csv'),parse_dates=[0])
print(df_date_parse['Date'])
df_date_parse = df_date_parse.set_index('Date')
print(df_date_parse)

# resample method is like grouping
print(df_date_parse.resample(rule='YE').mean())

# once csv is parsed with dates, can also call datetime methods
df_date_parse = pd.read_csv(os.path.join(os.path.dirname(__file__), 'SPY2000_2021.csv'),parse_dates=[0])
print(df_date_parse['Date'].dt.year)
