#from random import randint, choice
import random
# type conversion
pi = "3.14159"
pi = float(pi)
print(pi)

num = 1
num = float(num)
print(num)
print(str(num))

num = random.randint(1, 10)

if 3 <= num <= 5:
    print("Between 3 and 5")
    print(num)
elif 6 <= num <= 10: print("Between 6 and 10")
else: print("Not between 3 and 5")

# Assignment is to print "fruit", print "meat", or print "inedible"
food = random.choice(["apple", "grape", "bacon", "steak", "worm", "dirt"])
if food == "apple" or food == "grape":
    print(food, "fruit")
elif food == "bacon" or food == "steak":
    print(food, "meat")
else:
    print(food, "inedible")


actually_sick = random.choice([True, False])
kinda_sick = random.choice([True, False])
hate_your_job = random.choice([True, False])
sick_days = random.randint(0, 10)

''' 
calling_in_sick which will either be false or true depending on a few conditions
CONDITIONS:
Set to True if actually_sick and have sick_days remaining
Set to True if kinda_sick and hate_your_job and have sick_days remaining
Set to False otherwise
Print all the variables and their values!
'''
if actually_sick == True and sick_days > 0:
    calling_in_sick = True
elif kinda_sick == True and hate_your_job == True and sick_days >0:
    calling_in_sick = True
else:
    calling_in_sick = False
#print("Actually Sick: " + str(actually_sick) + " Sick Days: " + str(sick_days) + " Kinda Sick: " + str(kinda_sick) + " Hate Your Job: "+ str(hate_your_job))
#print(f"Actually Sick: {actually_sick} \nSick Days: {sick_days} \nKinda Sick: {kinda_sick} \nHate Your Job: {hate_your_job}")

# Java
# for (int i = 0; i < 10; i++) {
#     print(i)
# }
# Python
for i in range(0, 10):
    print(i)
i = 0
while i < 10:
    print(i)
    i+=1

# iterables in python: tuples, dictionaries, strings, lists, sets
# Sets are basically lists but they have no duplicate elements/values (unique elements)
l1 = [1, 3, 5, 3, 2, 1, 4]
food = ['apple', "grape", "bacon", "steak", "worm", "dirt"]
print(list(enumerate(food)))
for index, element in enumerate(food):
    if element == "grape":
        food[index] = "grapefruit"
    # print(element)
print(food)