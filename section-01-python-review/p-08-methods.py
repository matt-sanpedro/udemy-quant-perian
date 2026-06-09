# string methods
my_str = 'hello my name is Chuck Norris'
print(my_str.lower())
print(my_str.upper())

tweet = "Go Sports!  #cool"

# by default, the string split method returns a list split on the whitespace
print(tweet.split())

# dictionary methods
d = {'key': 10, 'key2': 'seconditem'}

# list of keys
print(d.keys())

# list methods
my_list = [num for num in range(1,4)]
print(my_list)

# appending an item to a list
my_list.append(4)
print(my_list)

# removing an item from a list (remove last item by default)
my_list.pop()
print(my_list)
my_list.pop(0)
print(my_list)

# check if an item exists in a list with the in method
print(2 in my_list)
print('a' in [0, 'A', 6])
print('a' in [0, 'a', 6])
