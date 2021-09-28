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
if (num_dict[first_properties] == "zero" or num_dict[first_houses] == "zero") and (num_dict[second_properties] == "zero" or num_dict[second_houses] == "zero"):
    print("You can't afford even one house")
elif num_dict[first_properties] == "zero" or num_dict[first_houses] == "zero":
    if second_houses >= 5:
        print(f"{num_dict[second_properties]} will have a hotel")
    else:
        print(f"{num_dict[second_properties]} will have {num_dict[second_houses]}")
elif num_dict[second_properties] == "zero" or num_dict[second_houses] == "zero":
    if first_houses >= 5:
        print(f"{num_dict[first_properties]} will have a hotel")
    else:
        print(f"{num_dict[first_properties]} will have {num_dict[first_houses]}")
else:
    if first_houses >= 5 and second_houses >= 5:
        print(f"{first_properties + second_properties} will have a hotel")
    elif first_houses >= 5:
        print(f"{num_dict[first_properties]} will have a hotel and {num_dict[second_properties]} will have {num_dict[second_houses]}")
    elif second_houses >= 5:
        print(f"{num_dict[first_properties]} will have {num_dict[first_houses]} and {num_dict[second_properties]} will have a hotel")
    else:
        print(f"{num_dict[first_properties]} will have {num_dict[first_houses]} and {num_dict[second_properties]} will have {num_dict[second_houses]}")

