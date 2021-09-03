import random

# random.randint(a, b)  a is the starting range, b is the end range (ALL INCLUSIVE)

user = input("Enter 'rock', 'paper', or 'scissors'")
computer = random.choice(["rock", "paper", "scissors"])
print(f"Computer chose {computer}!")
if computer == user:
    print("It is a tie")
elif computer == "rock":
    if user == "paper":
        print("You Win!")
    else:
        print("You Lose!")
elif computer == "paper":
    if user == "scissors":
        print("You Win!")
    else:
        print("You Lose!")
else:
    if user == "rock":
        print("You Win!")
    else:
        print("You Lose!")

# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0
for number in range(10, 20):
    if number%2 != 0:
        x += number
print(x)

from random import randint  # use randint(a, b) to generate a random number between 0 and 10
# print number of iterations it took to get five
import random
# store random number in here, each time through
iterations = 0
number = 0
while number != 5:
    number = randint(0, 10)
    iterations += 1
print(number, iterations)

# iterate through the list and count the number of ones, twos, and threes
ones = 0
twos = 0
threes = 0
l1 = [1,2,1,3,1,2,3,1] #len(l1) = 8
for number in l1:
    if number == 1:
        ones += 1
    if number == 2:
        twos += 1
    if number == 3:
        threes += 1
print(ones, twos, threes)

