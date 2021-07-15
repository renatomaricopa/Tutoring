# from random import randint

# dice_1 = randint(1,6)
# dice_2 = randint(1,6)
# count = 1
# print("		Dice 1 		Dice 2")
# if dice_1 == dice_2:
#     print("Toss 1		%d		%d" % (dice_1, dice_2))
#     print("1 toss to get doubles!") 
    
# while dice_1 != dice_2:
#     print("Toss %d		%d		%d" % (count, dice_1, dice_2))
#     dice_1 = randint(1,6)
#     dice_2 = randint(1,6)
#     count+=1
# print("Toss %d		%d		%d" % (count, dice_1, dice_2))
# print("%d toss to get doubles!" % count)



# # import math

# # Get the user to give you miles per hour
# mph = float(input("Please enter a speed at miles per hour: (enter 'quit' if you are finished) "))
# while mph != "quit":
#   # Convert mph into kph by using the equation below
#   kilometers = mph * 1.60934
#   # Display output with 4 decimal points to be precise
#   print()
#   print("%-7s"%"Kilometers per hour: ","%.4f"%kilometers)
#   mph = input("Please enter a speed at miles per hour: (enter 'quit' if you are finished) ")
#   try:
#     mph = float(mph)
#   except:
#     continue

from calendar import monthrange
# equality operators: !=, ==, <, >, <=, >=
#logical operators: and, or
year = 2021
finished = False
while True:
    month = int(input("Please input a valid number of month you were born: "))
    if month <= 12 and month >= 1:
        days_in_month = monthrange(year, month)[1]
        while True:
            day_born = int(input("Enter a valid number for the day you were born: "))
            if day_born <= days_in_month and day_born >= 1:
                if month == 1:
                    print("January", end=' ')
                elif month == 2: 
                    print("February", end=' ')
                elif month == 3: 
                    print("March", end= ' ')
                elif month == 4: 
                    print("April", end= ' ')
                elif month == 5: 
                    print("May", end= ' ')
                elif month == 6: 
                    print("June", end= ' ')
                elif month == 7: 
                    print("July", end= ' ')
                elif month == 8:
                    print("August", end= ' ')
                elif month == 9:
                    print("September", end= ' ')
                elif month == 10:
                    print("October", end= ' ')
                elif month == 11:
                    print("November", end= ' ')
                elif month == 12:
                    print("December", end= ' ')
                print(day_born)
                finished = True
                break
    if finished: break