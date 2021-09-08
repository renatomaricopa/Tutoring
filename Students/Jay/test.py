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