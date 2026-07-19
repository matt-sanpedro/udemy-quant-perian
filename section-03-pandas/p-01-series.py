import numpy as np
import pandas as pd

# Imaginary Sales Data for 1st and 2nd Quarters for Global Company
q1 = {'Japan': 80, 'China': 450, 'India': 200, 'USA': 250}
q2 = {'Brazil': 100,'China': 500, 'India': 210,'USA': 260}

sales_q1 = pd.Series(q1)
sales_q2 = pd.Series(q2)
print('Quarter one:\n{}\n\nQuarter two:\n{}'.format(sales_q1, sales_q2))

# accessing the Series elements
target_country = 'India'
print('{} sales for quarter one: {}'.format(target_country, sales_q1[target_country]))

# keys method
print(sales_q1.keys())

# since pandas Series are build on top of numpy arrays, can call broadcast operations
# demo: numpy array gets broadcasted
print(np.array([1,2]) * 2)

# if Series addition is performed, for labelled indices not present in both
print(sales_q1 + sales_q2)

# must call the built-in add method to define a fill_value
first_half = sales_q1.add(sales_q2, fill_value=0)
print('First half sales:\n{}'.format(first_half))

# performing pandas computations converts the data type to float
print(sales_q1.dtype)
print(first_half.dtype)
