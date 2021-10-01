#Alex Schmidt
#Program for Determining how many slices of pizza each person will get
#Determine how many pizzas are being ordered
# Strings: ""
# Primitive types: integers (1,2,-1), floats (3.14, 3.4), strings ("a", "Hello my name is"), booleans (True or False)

# print("Hello") # takes in a string and prints it out
# input("Give me a number") # takes in a string and prompts the user
# int() # convert something to an integer type

pizzas = int(input("# of pizzas being ordered: ")) # input will prompt the user to enter something in
people = int(input("# of people sharing pizzas: "))
slices = pizzas * 8

division = slices//people # 3
some_people = slices % people # 2
other_people = people - some_people # 3
new_division = division + 1
if some_people == 0:
    print(f"You will divide {slices} slices -- {people} will have {division}")
else:
    print(f"You will divide {slices} slices -- {some_people} will have {new_division} and {other_people} will have {division}")

# while True:
#     block_color = input("What color block will we be building on?").lower().strip()
#     if block_color in property_groups:
#         break
#     else:
#         print("Please enter a valid color")
# while True:
#     try:
#         money = int(input("How much money are you willing to spend?"))
#         break
#     except ValueError:
#         print("Please enter an integer")


# Dictionary is key, value pairs
property_groups = {"violet": [2, 50], "pale blue": [3, 50], "maroon": [3, 50], "orange": [3, 100], "red": [3, 150],
                   "yellow": [3, 150], "green": [3, 200], "dark blue": [2, 200]}
num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5:"five", 6: "six", 7:"seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}

block_color = input("What color block will we be building on?").lower().strip()
money = int(input("How much money are you willing to spend?"))
num_prop = property_groups[block_color][0] # number of properties per group
price_prop = property_groups[block_color][1]
print(f"There are {num_dict[num_prop]} properties and each house costs {price_prop}")
total_houses = money//price_prop
first_properties = total_houses % num_prop # some houses that get +1
second_properties = num_prop - first_properties # remaining houses that just get +0

second_houses = total_houses//num_prop
first_houses = second_houses + 1

print(f"You can build {total_houses} houses -- {num_dict[first_properties]} will have {num_dict[first_houses]} and {num_dict[second_properties]} will have {num_dict[second_houses]}")



