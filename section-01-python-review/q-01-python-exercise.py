# Given price = 300 , use python to figure out the square root of the price.
import math

price = 300
print(math.sqrt(300))

# Grab '500' from the string using indexing.
stock_index = "SP500"
print(stock_index[2:])

"""
** Given the variables:**

    stock_index = "SP500"
    price = 300

** Use .format() to print the following string: **

    The SP500 is at 300 today.
"""
print('The {stock} is at {price} today.'.format(stock=stock_index, price=price))

"""
** Given the variable of a nested dictionary with nested lists: **

    stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
    
** Use indexing and key calls to grab the following items:**

* Yesterday's SP500 price (250)
* The number 365 nested inside a list nested inside the 'info' key.
"""
stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
print(stock_info['sp500']['yesterday'])
print(stock_info['info'][1][2])

"""
### Task #5

** Given strings with this form where the last source value is always separated by two dashes -- **

    "PRICE:345.324:SOURCE--QUANDL"
    
**Create a function called source_finder() that returns the source. 
For example, the above string passed into the function would return "QUANDL"**
"""
def source_finder(string_data):
    return string_data.split("--")[-1]

print(source_finder("PRICE:345.324:SOURCE--QUANDL"))

"""
### Task #5

** Create a function called price_finder that returns True if the word 'price' is in a string. Your function should work even if 'Price' is capitalized or next to punctuation ('price!')  **
"""
def price_finder(string_data):
    return "price" in string_data.lower()

print(price_finder("What is the price?"))
print(price_finder("DUDE, WHAT IS PRICE!!!"))
print(price_finder("The price is 300"))

"""
### Task #6

** Create a function called count_price() that counts the number of times the word "price" occurs in a string. Account for capitalization and if the word price is next to punctuation. **
"""
s = 'Wow that is a nice price, very nice Price! I said price 3 times.'
# s = 'Wow that is a nice price, very nice Price! I said it 2 times.'
# s = 'Only one price here.'
# s = 'No hits here.'

def count_price(s):
    return s.lower().count("price")
    # return len(s.lower().split("price"))-1

print(count_price(s))

"""
### Task #7

**Create a function called avg_price that takes in a list of stock price numbers and calculates the average (Sum of the numbers divided by the number of elements in the list). It should return a float. **
"""
def avg_price(price_list):
    return sum(price_list)/len(price_list)

print(avg_price([3,4,5]))
