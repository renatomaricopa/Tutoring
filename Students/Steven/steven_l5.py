import random
'''
A single equal sign (=)is an assignment operator. It will assign a value to a variable.
A double equal sign (==) is an equality operator. It will check if two things are equal to each other.
'''

food = random.choice(['apple','grape', 'bacon', 'steak', 'molten lava', 'dirt'])
# Assignment is to print "fruit", print "meat", or print "inedible"

if food == "apple" or food == "grape":
    print(food, "fruit")
elif food == "bacon" or food == "steak":
    print(food, "meat")
else:
    print(food, "inedible")

print("tim" == "tim")
print(2*4 == 6)

''' 
calling_in_sick which will either be false or true depending on a few conditions
CONDITIONS:
Set to True if actually_sick and have sick_days remaining
Set to True if kinda_sick and hate_your_job and have sick_days remaining
Set to False otherwise
Print all the variables and their values!
'''
# randomly assigns values to these four variables
actually_sick = random.choice([True, False])
kinda_sick = random.choice([True, False])
hate_your_job = random.choice([True, False])
sick_days = random.randint(0, 10)
calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!




