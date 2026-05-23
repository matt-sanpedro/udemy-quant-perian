name = "Slim Shady"

print("Hello, my name is {}".format(name))

# number = "55"
number = 55

print("Hello, my name is {} and my number is {}".format(name, number))

# expanding on the print statement with variables
print("Hello, my name is {x} and my number is {y}".format(x=name, y=number))

# if the print statement is parameterized, then the order can change
print("Hello, my number is {y} and my name is {x}".format(x=name, y=number))

# taking it a step further with meaningful variables
print("Hello, my number is {num} and my name is {name}".format(name=name, num=number))
