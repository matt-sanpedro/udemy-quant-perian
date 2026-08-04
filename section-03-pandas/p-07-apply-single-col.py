import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'tips.csv'))
df.info()

# in python, cannot index integers but can cast it to a string
print(str(651651968511)[-4:])

# function that extracts has four values
def last_four(num): return str(num)[-4:]
print(last_four(123456789))

# apply the function to the 'CC Number' column
df['last_four'] = df['CC Number'].apply(last_four)
print(df[['CC Number', 'last_four']])

# determine mean
print(df['total_bill'].mean())

# yelp function to assign n amount of dollar signs depending 
def yelp(price):
    """
    assign n amount of dollar signs depending on the 'total_bill'
    """
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else:
        return '$$$'

# apply the yelp function to the 'total_price'
df['yelp'] = df['total_bill'].apply(yelp)
print(df[['total_bill', 'yelp']].head(10))
