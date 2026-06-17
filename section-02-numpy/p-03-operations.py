import numpy as np

arr = np.arange(0,10)

# arithmetic between arrays: on an element by element basis
print(arr + 5)

# for array addition, must be same shape
print(arr + arr)
print(arr / arr) # this will throw warning for the first index
print(1 / arr) # this will throw warning for dividing by zero
print(np.sqrt(arr))

# can also perform trigonometric functions
print(np.sin(arr))
print(np.log(arr))

# sum and mean methods
print(arr.sum())
print(arr.mean())
print(arr.max())

# variance and standard deviation
print(arr.var())
print(arr.std())

arr2d = np.arange(0,25).reshape(5,5)
print(arr2d.shape)

# perform sum across the rows
print(arr2d.sum(axis=0))

# perform sum across the columns
print(arr2d.sum(axis=1))
