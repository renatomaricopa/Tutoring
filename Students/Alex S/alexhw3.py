property_groups = {"violet": [2, 50], "pale blue": [3, 50], "maroon": [3, 50], "orange": [3, 100], "red": [3, 150],
                   "yellow": [3, 150], "green": [3, 200], "dark blue": [2, 200]}
num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve"}

block_color = input("What color block will we be building on?").lower().strip()
money = int(input("How much money are you willing to spend?"))
num_prop = property_groups[block_color][0]
# number of properties per group
#refer to dict for #of props and price per prop
price_prop = property_groups[block_color][1]
#print statement for properties and cost per house
print(f"There are {num_dict[num_prop]} properties and each house costs {price_prop}")
#determine how many properties can be built with th alotted money
num_houses = money//price_prop
#determine how many houses will be on the property that is leftover
some_houses = num_houses % num_prop
other_houses = some_houses - 1 
even_more_houses = num_houses//num_prop
the_most_houses = even_more_houses + 1
print(f"You can build {num_dict[num_houses]} houses -- {num_dict[some_houses]} will have {num_dict[the_most_houses]} and {num_dict[other_houses]} will have {num_dict[even_more_houses]}")
