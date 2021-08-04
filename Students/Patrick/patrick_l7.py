#dont forget to put in a main() function at the top to organize all the functions a little better

# def has_at_least_one_upper(password):
#     for character in password:
#         if character.isupper():
#         	return True
#     return False

# def has_at_least_one_lower(password):
#     for character in password:
#         if character.islower():
#         	return True
#     return False
  
# def has_at_least_one_digit(password):
#     for character in password:
#         if character.isdigit():
#         	return True
#     return False

# def has_at_least_one_symbol(password):
#   if any(not character.isalnum() for character in password):
#   	return True
#   return False
  
# def at_least_ten_characters(password):
#   if len(password) >= 10:
#   		return True
#   return False
	
# def main():
#     password = input("Please enter a password: ")
#     ten = at_least_ten_characters(password)
#     upper = has_at_least_one_upper(password)
#     lower = has_at_least_one_lower(password)
#     symbol = has_at_least_one_symbol(password)
#     digit = has_at_least_one_digit(password)

#     l1 = [upper, lower, symbol, digit]

#     if not ten:
#         print("Too short. ", end="")
#     if not upper or not lower or not symbol or not digit:
#         print("Does not contain at least", end="")
#     # if not upper:
#     #     print("Does not contain at least one uppercase. ", end="")
#     # if not lower:
#     #     print("Does not contain at least one lowercase. ", end="")
#     # if not symbol:
#     #     print("Does not contain at least one symbol. ", end="")
#     # if not digit:
#     #     print("Does not contain at least one digit. ", end="")
#     # if upper and lower and symbol and digit:
#     #     print("Strong Password.")
# main()

def get_sales():
  sales = []
  days = ["monday", "tuesday", "wednesday", "thursday", "friday"]
  for day in days:
    sale = input(f"Please enter your sales for {day}: ")
    if sale.isnumeric() and int(sale) > 0:
      sale = int(sale)
      sales.append(sale)
  return sales, days

# function definition
def display(sales, days):
    maxSales = 0
    maxIndex = 0
    print("Monday Tuesday Wednesday Thursday Friday")
    for index, sale in enumerate(sales):
        print(f"${sale}", end="       ")
        if sale > maxSales:
            maxSales = sale
            maxIndex = index
    print(" ")
    print(f"Total = ${sum(sales)}")
    print(f"Average = ${sum(sales)/5}")
    print(f"Max Sales/Day = ${maxSales}/{days[maxIndex]}")
  
  
  
def main():
  sales, days = get_sales()
  display(sales, days)

main()






