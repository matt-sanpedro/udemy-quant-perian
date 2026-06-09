# function with default parameter and docstring
def my_func(param="Superman"):
    """
    Docstring goes in here!

    """
    print(param)

my_func("Michael Jackson")

# function with return statement
def assign_var(argument):
    return argument**2

x = assign_var(5)
print(x)

# lambda function: an anonymous function with no name that can be used one time
lambda var: var*2

# create a sequence of numbers (1 to 5) using the range function and list comprehension
seq = [i for i in range(1,6)]
print(seq)

# the map function
print(map(lambda var: var*2, seq))
print('type: {}'.format(type(map(lambda var: var*2, seq))))

# cast the map function into a list to see the results
print(list(map(lambda var: var*2, seq)))

# the filter function and examples
def is_even(num):
    return num%2 == 0
print(is_even(6))

# cast the filter function into a list to see the results
print(list(filter(is_even, seq)))

# the filter function using a lambda expression
print(list(filter(lambda num: num%2==0, seq)))
