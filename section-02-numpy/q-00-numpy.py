#### 1. Import NumPy as np
import numpy as np

#### 2. Create an array of 10 zeros 
arr_zeros = np.zeros(10)
print(arr_zeros)

#### 3. Create an array of 10 ones
arr_ones = np.ones(10)
print(arr_ones)

#### 4. Create an array of 10 fives
arr_fives = np.full(10, 5.0)
print(arr_fives)

#### 5. Create an array of the integers from 10 to 50
arr_int = np.arange(10, 51)
print(arr_int)

#### 6. Create an array of all the even integers from 10 to 50
arr_evens = np.arange(10,51,2)
print(arr_evens)

#### 7. Create a 3x3 matrix with values ranging from 0 to 8
arr = np.arange(0,9)
print(arr)
arr = arr.reshape(3,3)
print(arr)

#### 8. Create a 3x3 identity matrix
mat_i = np.eye(3)
print(mat_i)

#### 9. Use NumPy to generate a random number between 0 and 1
# NOTE: Your result's value should be different from the one shown below.
print(np.random.rand(1))

#### 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution<br><br>&emsp;&ensp;NOTE: Your result's values should be different from the ones shown below.
print(np.random.randn(25))

#### 11. Create the following matrix:
"""
array([[0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1 ],
       [0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2 ],
       [0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3 ],
       [0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4 ],
       [0.41, 0.42, 0.43, 0.44, 0.45, 0.46, 0.47, 0.48, 0.49, 0.5 ],
       [0.51, 0.52, 0.53, 0.54, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6 ],
       [0.61, 0.62, 0.63, 0.64, 0.65, 0.66, 0.67, 0.68, 0.69, 0.7 ],
       [0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.78, 0.79, 0.8 ],
       [0.81, 0.82, 0.83, 0.84, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9 ],
       [0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1.  ]])
"""
print(np.arange(0.01, 1.01, 0.01).reshape(10,10))

#### 12. Create an array of 20 linearly spaced points between 0 and 1:
print(np.linspace(0,1,20))

#### 13. Write code that reproduces the output shown below.
# Be careful not to run the cell immediately above the output, otherwise you won't be able to see the output any more.
"""
array([[12, 13, 14, 15],
       [17, 18, 19, 20],
       [22, 23, 24, 25]])
"""
print(np.array(([12,13,14,15],[17,18,19,20],[22,23,24,25])))

#### 14. Write code that reproduces the output shown below.
print(20)

#### 15. Write code that reproduces the output shown below.
"""
array([[ 2],
       [ 7],
       [12]])
"""
print(np.array(([2],[7],[12])))

#### 16. Write code that reproduces the output shown below.
"""
array([21, 22, 23, 24, 25])
"""
print(np.arange(21,26))

#### 17. Write code that reproduces the output shown below.
"""
array([[16, 17, 18, 19, 20],
       [21, 22, 23, 24, 25]])
"""
print(np.array(([16, 17, 18, 19, 20],[21, 22, 23, 24, 25])))

#### 18. Get the sum of all the values in mat
print(np.array(([16, 17, 18, 19, 20],[21, 22, 23, 24, 25])).sum())
