# for loop using the range function
for i in range(5):
    print(i, end=" ")

# changing the increments with the range function
print("\n")
for i in range(0,20,2):
    print(i, end=" ")

# appending to a list
x = []
for i in range(5):
    x.append(i)
print("\n{}".format(x))

# list comprehension
print([num**2 for num in x])
