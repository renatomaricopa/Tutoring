'''
Write a while loop to keep regenerating a new random number between 1 and 10 as long as the random number is not 5!
'''
# --------------------------------------------------------------------------------
from random import randint
import random

number = 0
counts = 0
while number != 5:
    number = random.randint(1, 15)
    print(number)
    counts += 1
print("Counts:", counts)
# ---------------------------------------------------------------------------------
'''
Create an empty list. Add 4 different types of objects to the list. (e.g. float, integer, string, boolean)
'''
# Create empty list
voters_for_tim = []

# Append to empty list
voters_for_tim.append("Jay")

popularity = 837509.9405
voters_for_tim.append(popularity)
popularity2 = 999
voters_for_tim.append(popularity2)
tim_is_cool = True
voters_for_tim.append(tim_is_cool)
voters_for_tim.append("Jay")
print(voters_for_tim)
# Insert and remove at index (update the index with a new value)
length_of_list = len(voters_for_tim)
index = 4
voters_for_tim.insert(index, "Andy")
print(voters_for_tim)
voters_for_tim.pop(index + 1)
print(voters_for_tim)
'''
Replace the first and second elements in our list with "Andy" and 10.0
'''
voters_for_tim[1] = 10
print(voters_for_tim)
print("Length:", length_of_list)

