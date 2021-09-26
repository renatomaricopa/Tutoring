'''
Add up every odd number from 10 - 20 (inclusive) and store the result in a variable called "answers"
Hints: Use "range()" and "for loop"
'''
import time
import random

answers = 0
for i in range(11, 21, 2):
    answers += i
    print("answers:", answers, "i:", i)


l1 = []
for i in range(0, 100):
    l1.append(random.randint(1, 3))

# I want you to count the number of ones, twos, and threes in the list using a for loop and if/else statements
ones = 0
twos = 0
threes = 0
for number in l1:
    if number == 3:
        threes += 1
    elif number == 1:
        ones += 1
    else:
        twos += 1

print(l1)

print("ones: ", ones)
time.sleep(1)
print("twos: ", twos)
time.sleep(1)
print("threes: ", threes)

if ones > twos:
    if ones > threes:
        print("the winner is the ones! It will get a free trip to hawaii beach!")
    elif ones == threes:
        print("tie between ones and threes")
    else:
        print("the winner is threes! It will earn one dodecillion whole pizzas!")
else:
    if twos > threes:
        print("the winner is the twos! It will get a free trip to hawaii beach!")
    elif twos == threes:
        print("tie between twos and three")
    else:
        print("the winner is threes! It will earn 9999999999999 dollars")

'''
Write a while loop to keep regenerating a new random number between 1 and 10 as long as the random number is not 5!
'''
# Hey, I'm in the zoom call already
# click on the link in the google calendar
# https://us04web.zoom.us/j/77626024488?pwd=Z3grWEtoVUNYbGhXSzYrOWIvN0ZGZz09
#The zoom said "The host has another meeting in process"
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
