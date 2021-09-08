# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| \
from random import randint                           #|  \
x = randint(-100, 100)                               #|   \
while x == 0:  # make sure x isn't zero              #|    \
    x = randint(-100, 100)                           #|     NO TOUCHING!!!!!! (please)
y = randint(-100, 100)                               #|    /
while y == 0:  # make sure y isn't zero              #|   /
    y = randint(-100, 100)                           #|  /
# NO TOUCHING==NO TOUCHING==NO TOUCHING==NO TOUCHING #| /

# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
print(x, y)
if x > 0 and y > 0:
    print("both positive")
elif y < 0 < x:  # we can simplify this  x > 0 and y < 0 == y < 0 < x
    print("x is positive and y is negative")
elif x < 0 and y < 0:
    print("both negative")
else:
    print("x is negative and y is positive")

# YOUR CODE GOES HERE ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^