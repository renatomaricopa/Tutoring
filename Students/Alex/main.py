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
