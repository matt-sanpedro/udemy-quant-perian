import numpy as np

arr = np.arange(0,11)
print(arr)

# select a single value
print(arr[2])

# similar to arrays, can also slice
print(arr[2:])
print(type(arr[2:]))

# broadcast a single value across a larger set of values
arr[:5] = 100
print(arr)

# replicating this for a normal python list
mylist = list(range(0,11))
print(mylist[:5])
mylist[:5] = [1000, 1000, 1000, 1000, 1000]
print(mylist)

# slicing an numpy array
slice_of_arr = arr[:5]
print(slice_of_arr)
slice_of_arr[:] = 99
print(slice_of_arr)

# copy method on numpy arrays
arr_copy = arr.copy()
print(arr)
arr_copy[:] = 77
print(arr_copy)

# call the shape method to return row, col
arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)
print(arr_2d.shape)

# return the first row of the 2d array
print(arr_2d[0])

# two ways to extract the indices
print(arr_2d[1][1])
print(arr_2d[1,1])

# can also slice to extract subsection
print(arr_2d[:2,1:])

# numpy array conditional selection by broadcasting
arr = np.arange(1,11)
print(arr)
bool_arr = arr > 4

# use the bool_arr as a filter
print(arr[bool_arr])
print(arr[arr > 4])
