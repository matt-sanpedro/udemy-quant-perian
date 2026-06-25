import numpy as np

# converting a python list to numpy array
mylist = list(range(1,4))
print(mylist)

myarray = np.array(mylist)
print(myarray)
print(type(myarray))

# nested list
my_matrix = [[1,2,3], [4,5,6], [7,8,9]]

# converted to numpy array, 
print(np.array(my_matrix))
"""
3 rows, 3 columns in a 2D array ()

OUTPUT: 

[[1 2 3]
 [4 5 6]
 [7 8 9]]
"""

# instead of casting python lists into an array, numpy has built in functions/methods
# similar to python range function
print(np.arange(0,10,2))

# create arrays of zero's of float data type
print(np.zeros(5))
print(np.zeros((2,6))) # (rows, columns)

# similar can create arrays of one's
print(np.ones((3,4)))

# evenly spaced numbers over a specified interval
print(np.linspace(0,10,21))

# can call the len function on the numpy array
print(type(np.linspace(0,10,21)))
print('The length of the numpy array is: {}'.format(len(np.linspace(0,10,21))))

# create an identity matrix with the eye function
print(np.eye(5))

# generating random data
print(np.random.rand(1))
print(np.random.rand(3,6))

# create samples from a standard normal distribution (numbers closer to zero likely drawn)
print(np.random.randn(1))
print(np.random.randn(2,4))

# generating random integers
print(np.random.randint(0,101,5))
print(np.random.randint(0,101,(3,3)))

# seed function returns the same data set (important for repeating random distributions)
print('Calling the seed function')
np.random.seed(42)
store_set = np.random.rand(4)
print(store_set)
print(np.random.rand(4)) # no longer same as "store_set" but values are consistent
print(store_set)

# attribute and method calls
# reshape with rows and columns arguments
arr = np.arange(0,25)
print(arr)
arr = arr.reshape(5,5)
print(arr)

# find the min/max value and indices in a random generated numpy array
ranarr = np.random.randint(0,101,10)
print(ranarr)
print('The max is: {}, the index is: {}'.format(ranarr.max(), ranarr.argmax()))
print('The min is: {}, the index is: {}'.format(ranarr.min(), ranarr.argmin()))

# output the data type
print(ranarr.dtype)

# check the shape size
print(ranarr.shape)
print(arr.shape)
