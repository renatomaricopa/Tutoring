import time
print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

print("SHOOT!")

if player1 == "rock" and player2 == "paper":
    print("the winner is...")
    time.sleep(5)
    print("is player2!")
elif player1 == "paper" and player2 == "rock":
    print("the winner is...")
    time.sleep(5)
    print("is player1!")
elif player1 == "scissor" and player2 == "paper":
    print("the winner is...")
    time.sleep(5)
    print("is player1!")
