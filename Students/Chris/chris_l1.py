# data structures: lists, dictionaries, global variables that we already know, sets, tuples
primary_colors = ("Red", "Blue", "Yellow")
orange = ("Red", "Yellow")
purple = ("Red", "Blue")
green = ("Yellow", "Blue")

first_color = input("Select Red, Blue, Yellow: ")
second_color = input("Select Red, Blue, Yellow: ")

if first_color == second_color:
    print("Error: Same colors entered!")
else:
    if first_color in primary_colors and second_color in primary_colors:
        if first_color in orange and second_color in orange:
            print("Orange")
        if first_color in purple and second_color in purple:
            print("Purple")
        if first_color in green and second_color in green:
            print("Green")
        else:
            print("ERROR: one of these or both are not a valid color!")
