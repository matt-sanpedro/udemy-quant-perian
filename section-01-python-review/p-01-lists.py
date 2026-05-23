my_list = ['a', 'b', 'c', 'd']

# can use postive and negative indexing
print("The zeroth index value: {}.  The last index value: {}.".format(my_list[0], my_list[-1]))

# list slicing is also supported
# the first number is the starting index and the second number is the stopping index (not inclusive)
print(my_list[0:2])

# slicing with negative indexing
print(my_list[0:-1])

# if the stopping index is left blank, it will go to the end of the list
print(my_list[0:])

# nested list example
nested_list = [1, 2, ['a', 'b', 'c']]
print(nested_list[2][1]) #b
