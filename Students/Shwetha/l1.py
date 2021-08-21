import math
import random
# Define a variable named city and set it equal to any string
city = "Hello, my name is Shwetha."

# Define a variable named price and set it equal to any float
price = 50.32



# Define a variable named high_score and set it equal to any int
high_score = 509

# Define a variable named is_having_fun and set it to a Boolean value
is_having_fun = False


# I want to you to divide cash by 5, store it in a variable named divided_cash, and print it out to the console
cash = 19867324678987.99  # DON'T CHANGE THE CASH VARIABLE

divided_cash = cash/5
print(divided_cash)

# Arithmetic operators
# +, -, /, *, **, %, //
print(3**2)
# this is good if we only want an integer value
print(5//2)

# get the ceiling of 5/2 and print it out
print(math.ceil(5/2))
print(random.randint(1, 10))

# You can initialize to "", 0, [], None, -999999999999
# string concatenation uses the "+" operator
greeting = "Hello"
name = "Sneha"
# greet_name = greeting + " " + name
# f string!
greet_name = f"{greeting} {name}"
print(greet_name)

number = 3.1415926
print(f"{number:.2f}")

# string slicing
computer = "apple computer"
apple_list = computer.split(" ")
print(apple_list)
apple_list[0] = apple_list[0]
apple_list[1] = apple_list[1][::-1]
new_string = "".join(apple_list)
print(new_string)

# string formatting
first = "Tim"
last = "Sim"
middle = "Fra"

formatted = "First Name: {f}, Middle Name: {m}, Last Name: {l}".format(f=first, l=last, m=middle)
print(formatted)


# docstrings
'''
asdfjkasdjfl
asjdkflajlsd
aklsdf
'''







