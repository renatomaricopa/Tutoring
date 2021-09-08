import time
import random

jay = 0
tim = 0
i = 0
count = 0
turn = "Jay"
while count < 10:
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input(f"(Enter {turn}'s choice): ")
    computer = random.choice(["rock", "paper", "scissors"])

    print("SHOOT!")
    if player == computer:
        time.sleep(1)
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("the winner is...")
            time.sleep(1)
            print("is computer!")
            i -= 1
        else:
            print("the winner is...")
            time.sleep(1)
            print(f"is {turn}!")
            i += 1
    elif player == "paper":
        if computer == "scissors":
            print("the winner is...")
            time.sleep(1)
            print("is computer!")
            i -= 1
        else:
            print("the winner is...")
            time.sleep(1)
            print(f"is {turn}!")
            i += 1
    elif player == "scissors":
        if computer == "paper":
            print("the winner is...")
            time.sleep(1)
            print(f"is {turn}!")
            i += 1
        else:
            print("the winner is...")
            time.sleep(1)
            print("is computer!")
            i -= 1
    if turn == "Tim":
        tim += i
        turn = "Jay"
    else:
        jay += i
        turn = "Tim"
    i = 0
    print(f"The computer chose {computer}!")
    print(f"Tim has {tim} points and Jay has {jay} points!")
    count += 1
    print(f"Turns left = {10 - count}")
if jay > tim:
    print("Jay won THE GRAND FINALE!")
elif tim > jay:
    print("Tim won THE GRAND FINALE!")
else:
    print("It's a tie!")