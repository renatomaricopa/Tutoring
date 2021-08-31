# import the random module
# use "winnings = random.randint(2, 10)" to generate a random int from 2 - 10 and store in a variable "winnings"
import random
# unit price of a lottery ticket
constant_lottery_unit_price = 2 # integer
# unit price of an apple
constant_apple_unit_price = .99
# unit price of a can of beans
constant_canned_beans_unit_price = 1.58
# unit price of a soda
constant_soda_unit_price = 1.23
# the user has initial $5 for shopping
money = 5
# the user has spent $0 initially
money_spent = 0
# the amounts of lottery tickets, apples, cans of beans, and sodas the user has purchased
lottery_amount, apple_amount, canned_beans_amount, soda_amount = 0, 0, 0, 0

print("Welcome to the supermarket! Here's what we have in stock:")
print("Lottery tickets cost $" + str(constant_lottery_unit_price) + " each")
print("Cans of beans cost $" + str(constant_canned_beans_unit_price) + " each")
print("Apples cost $" + str(constant_apple_unit_price) + " each")
print("Sodas cost $" + str(constant_soda_unit_price) + " each")
print(f"You have ${money} available") # this is called f string
user_input = input(f"First, do you want to buy a ${constant_lottery_unit_price} lottery ticket for a chance at winning $2-$10? (y/n)")
if user_input == "y":
  winnings = random.randint(2, 10)
  money = money + winnings - constant_lottery_unit_price
  money_spent = money_spent + constant_lottery_unit_price
  print(f"Congrats! You won ${winnings}!")

print(f"You have ${money} available")
user_input = input("Do you want to buy apple(s)? (y/n)")
if user_input == "y":
  amount_apples = input("How many apple(s) do you want to buy?")
  cost = amount_apples*constant_apple_unit_price
  print(f"The user wants to buy {amount_apples} apple(s). This will cost ${cost}.")
  if money - cost >= 0:
    print(f"The user has enough money. {amount_apples} apple(s) purchased.")
  else: print("Not enough money! No apples purchased.")
    