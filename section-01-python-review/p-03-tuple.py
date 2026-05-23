# similar to a list but is immutable (cannot be changed after creation)
t = (1,2,3)
print(type(t))

# can be indexed and sliced like a list
print(t[0:])

# in the otherhand, a list is muutable and supports item reassignment
my_list = [1,2,3]
print(my_list)
my_list[0] = 'NEW'
print(my_list)
