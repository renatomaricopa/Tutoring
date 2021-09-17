number = input()
number2 = input()
number3 = input()

if number < number2:
  if number < number3:
    print(number)
  elif number > number3:
    print(number3)
elif number > number2:
  if number2 < number3:
    print(number2)
  elif number2 > number3:
    print(number3)

'''
# Print invalid if invalid day or month
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
'''

input_month = input()
input_day = int(input())

months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31, "Spetember": 30, "October": 31, "November": 30, "December": 31}

if input_month in months:
  if input_month == "January":
    if input_day <= months[input_month]:
      print("Winter")
    else:
      print("Invalid")
  if input_month == "February":
    if input_day <= months[input_month]:
      print("Winter")  
    else:
      print("Invalid")     
  if input_month == "March":
    if 1 <= input_day <= 19:
      print("Winter")
    else if 20 <= input_day <= months[input_month]:  
      print("Spring")
    else:
      print("Invalid)
else:
  print("Invalid")