"""Name: Evelyn D.
ID: 52208328
Statement of Work: Course materials referenced. Worked without outside help"""

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
if user_input.lower() == "y":
  number = random.randint(0,2)
  winnings = 0
  if number == 1: # if they win
    winnings = random.randint(2, 10)
    print(f"Congrats! You won ${winnings}!")
  else: print ("No lottery tickets won")
  money_spent = money_spent + constant_lottery_unit_price
  money = money + winnings - constant_lottery_unit_price
  lottery_amount = lottery_amount + 1
else: print("No lotery tickets were purchased.")

print(f"You have ${money} available")
user_input = input("Do you want to buy apple(s)? (y/n)")
if user_input.lower() == "y":
  apples_bought = input("How many apple(s) do you want to buy?") 
  if apples_bought.isdigit(): # if an integer
    apple_bought = int(apple_bought) # change to number (because we know it is a numerical value)
    cost = apples_bought*constant_apple_unit_price
    print(f"The user wants to buy {apples_bought} apple(s). This will cost ${cost}.")
    if money - cost >= 0: # if they have enough money
      print(f"The user has enough money. {apples_bought} apple(s) purchased.")
      money = money - cost
      apple_amount = apple_amount + apples_bought
    else: print("Not enough money! No apples purchased.")
  else: print("Only numerical values are accepted.")
else: print ("No apples were purchased.")
  
print(f"You have ${money} available")
user_input = input("Do you want to buy can(s) of beans? (y/n)")
if user_input.lower() == "y":
  beans_bought = input("How many can(s) of beans do you want to buy?") 
  if beans_bought.isdigit(): # if an integer
    beans_bought = int(beans_bought) # change to number (because we know it is a numerical value)
    cost = beans_bought*constant_canned_beans_unit_price
    print(f"The user wants to buy {beans_bought} can(s) of beans. This will cost ${cost}.")
    if money - cost >= 0: # if they have enough money
      print(f"The user has enough money. {beans_bought} can(s) of beans purchased.")
      money = money - cost
      beans_amount = beans_amount + beans_bought
    else: print("Not enough money! No can(s) of beans purchased.")
  else: print("Only numerical values are accepted.")
else: print ("No can(s) of beans were purchased.")
  
  print(f"You have ${money} available")
user_input = input("Do you want to buy sodas? (y/n)")
if user_input.lower() == "y":
  sodas_bought = input("How many sodas do you want to buy?") 
  if sodas_bought.isdigit(): # if an integer
    sodas_bought = int(sodas_bought) # change to number (because we know it is a numerical value)
    cost = sodas_bought*constant_soda_unit_price
    print(f"The user wants to buy {sodas_bought} sodas. This will cost ${cost}.")
    if money - cost >= 0: # if they have enough money
      print(f"The user has enough money. {sodas_bought} sodas purchased.")
      money = money - cost
      sodas_amount = sodas_amount + sodas_bought
    else: print("Not enough money! No sodas purchased.")
  else: print("Only numerical values are accepted.")
else: print ("No sodas were purchased.")
  
print(f"You have ${money} available")
print(f"You bought {apples_amount} apples")
print(f"You bought {beans_amount} can(s) of beans")
print(f"You bought {sodas_amount} sodas")
  