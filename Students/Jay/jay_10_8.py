# # 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
# number = (1, 2, 3, 4)
#
# # 2 - Create a variable called value which is a tuple with the the value 1 inside.
# value = (1)
# # 3 - Given the following variable:
# values = [10,20,30]
#
# # Create a variable called static_values which is the result of the values variable converted to a tuple
# static_values = tuple(values)
#
# # 4 - Given the following variable
#
# stuff = [1,3,1,5,2,5,1,2,5]
#
# # Create a variable called unique_stuff which is a set of only the unique values in the stuff list
# unique_stuff = set(stuff)
#
# print(static_values, unique_stuff)

import turtle
wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
my_pleasure = turtle.Turtle()
my_pleasure.ht()
my_pleasure.penup()
my_pleasure.goto(-100,100)
my_pleasure.pendown()
for _ in range(5):
    my_pleasure.forward(300)
    my_pleasure.right(144)
my_pleasure.write("Jay", font=("Freestyle Script", 60, "normal"))
turtle.done()
