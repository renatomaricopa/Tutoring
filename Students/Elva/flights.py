import mysql.connector
import sys

# connects to the database and fetching the data from the table
def getDataFromDatabase():
    try:
        conn = mysql.connector.connect(
            user="airlineXreader",
            password="GB5zo5WzS0GTx&R4TY",
            host="wi-winf.htwsaar.de",
            port=13307,
            database="airlineX"
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

    # Get Cursor
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute("SELECT * FROM flightbookings ORDER BY price DESC")

    # convert the result to a list of tuples
    rows = list(cur)

    # generate an empty list
    resultList = []
    for row in rows:
        resultList.append(list(row))

    # close the db connection
    cur.close()
    conn.close()

    return resultList

# filters the given list
# returns a list with "Economy class" bookings only
#def filterEconomyClass(bookingList):
#    newList = filter(lambda x: [row for row in bookingList if (x[5] == 'Y' and x[0] > 35)], bookingList)
#    return list(newList)

# Our program starts here

# Function to input the number of travellers for each class:
def ticketInput():
    entry1 = '\n Let me know the number of travelers for First Class: '
    firstClassNumber = int(input(entry1))
    print('\n Booking for First Class accepted - Thank you!')

    entry2 = '\n Let me know the number of travelers for Business Class: '
    businessClassNumber = int(input(entry2))
    print('\n Booking for Business Class accepted - Thank you!')

    entry3 = '\n Let me know the number of travelers for Economy Class: '
    economyClassNumber = int(input(entry3))
    print('\n Booking for Economy Class accepted - Thank you!')
    print()
    print()
    return firstClassNumber, businessClassNumber, economyClassNumber

# filtering first class list in order of priority

def FilterFirstClass(bookingList, FCresult, FCavailableSeat):
    for x in list(bookingList): # this creates a copy that we can freely iterate/loop through.
        if FCavailableSeat == 0:
            return
        else:
            # first class, senator status, female
            if x[5] == 'F' and x[8] == 1 and x[3] == 'F' and x[4] < 2003:
                x[9] = "F1"
                FCresult.append(x)
                FCavailableSeat -= 1
    # bookingList = list(filter(lambda x: x not in FCresult, bookingList)

    for x in list(bookingList):
        if FCavailableSeat == 0:
            return
        else:
            if x[5] == 'F' and x[8] == 0 and x[3] == 'F' and x[4] < 2003:
                x[9] = "F2"
                FCresult.append(x)
                bookingList.remove(x)
                FCavailableSeat -= 1

    for x in list(bookingList):
        if FCavailableSeat == 0:
            return
        else:
            if x[5] == 'F' and x[8] == 0 and x[3] == 'F' and x[7] > 7000:
                x[9] = "F3"
                FCresult.append(x)
                bookingList.remove(x)
                FCavailableSeat -= 1

    for x in list(bookingList):
        if FCavailableSeat == 0:
            return
        else:
            if x[5] == 'F' and x[8] == 1 and x[3] == 'M' and x[4] < 2003 and x[1] <= 'U':
                x[9] = "F4"
                FCresult.append(x)
                bookingList.remove(x)
                FCavailableSeat -= 1

    for x in list(bookingList): # iterator is like a loop (e.g. a for loop). iterable is what the loop loops through (e.g. a list or a string).
        print(FCavailableSeat) # an iterator iterates/loops through an iterable.
        if FCavailableSeat == 0:
            return
        else:
            if x[5] == 'F':
                x[9] = "F5"
                FCresult.append(x)
                bookingList.remove(x)
                FCavailableSeat -= 1
    

#Defning functions to filter Business Class in order of priority
def FilterBusinessClass(bookingList, BCresult, BCavailableSeat):
    number = []
    i = 1
    for x in bookingList:
        if BCavailableSeat == 0:
            return
        else:
            #First Priority criteria is the passengers who booked business, are females, born before 1990
            # and have frequent flyer status 1
            if x[5] == 'B' and x[3] == "F" and x[4] < 1990 and x[8] > 0:
                x[9] = "B1"
                x.append(i)
                BCresult.append(x)
                i += 1
                bookingList.remove(x)
                BCavailableSeat -= 1
            
    for x in list(bookingList):
        if BCavailableSeat == 0:
            return
        else:
            # Second Priority criteria is the passengers who booked business, are males, paid ticket> 935
            # and have frequent flyer status 1
            if x[5] == 'B' and x[3] == "M" and x[6] > 935 and x[8] > 0:
                x[9] = "B2"
                x.append(i)
                BCresult.append(x)
                i += 1
                bookingList.remove(x)
                BCavailableSeat -= 1

    for x in list(bookingList):
        if BCavailableSeat == 0:
            return
        else:
            # Third Priority criteria is the passengers who booked business, the ticket Id <3000 and
            # have frequent flyer status 1
            if x[5] == 'B' and x[7] <3000 and x[8] > 1:
                x[9] = "B3"
                x.append(i)
                BCresult.append(x)
                i += 1
                bookingList.remove(x)
                BCavailableSeat -= 1

    for x in list(bookingList):
        if BCavailableSeat == 0:
            return
        else:
            # Fourth Priority criteria is the passengers who booked business, are males, their surnames start between A and H
            # and have frequent flyer status 1
            if x[5] == 'B' and x[3] == "M" and x[1] > "H" and x[8] > 0:
                x[9] = "B4"
                x.append(i)
                BCresult.append(x)
                i += 1
                bookingList.remove(x)
                BCavailableSeat -= 1

    for x in list(bookingList):
        if BCavailableSeat == 0:
            return
        else:
            # Fifth Priority criteria is the all the rest passengers who booked business
            if x[5] == 'B':
                x[9] = "B5"
                x.append(i)
                BCresult.append(x)
                i += 1
                bookingList.remove(x)
                BCavailableSeat -= 1


# filtering economy class list in order of priority
def FilterEconomyClass(bookingList, ECresult, ECavailableSeat):
    for x in list(bookingList):
        if ECavailableSeat == 0:
            return
        else:
            # economy class, male, price >540
            if x[5] == 'Y' and x[6] >= 540 and x[3] == "M":
                x[9] = "Y1"
                ECresult.append(x)
                bookingList.remove(x)
                ECavailableSeat -= 1

    for x in list(bookingList):
        if ECavailableSeat == 0:
            return
        else:
            # economyclass, frequent flyer, born before 2000
            if x[5] == 'Y' and x[4] < 2000 and x[8] == 1:
                x[9] = "Y2"
                ECresult.append(x)
                bookingList.remove(x)
                ECavailableSeat -= 1

    for x in list(bookingList):
        if ECavailableSeat == 0:
            return
        else:
            # economyclass, ticket number >5000, last name start with >H
            if x[5] == 'Y' and x[7] > 5000 and x[1] > "H":
                x[9] = "Y3"
                ECresult.append(x)
                bookingList.remove(x)
                ECavailableSeat -= 1

    for x in list(bookingList):
        if ECavailableSeat == 0:
            return
        else:
            # economyclass, first name starts > I, price > 400
            if x[5] == "Y" and x[2] > "I" and x[6] > 400:
                x[9] = "Y4"
                ECresult.append(x)
                bookingList.remove(x)
                ECavailableSeat -= 1
                
    for x in list(bookingList):
        if ECavailableSeat == 0:
            return
        else:
            if x[5] == 'Y':
                x[9] = "Y5"
                ECresult.append(x)
                bookingList.remove(x)
                ECavailableSeat -= 1

# Calculating average price and total price
def averagePrice(result):
    if len(result) == 0:
        return 0
    else:
        sum = 0  # starting from 0
        for x in result:
            sum += x[6]
        return sum / len(result)

# Summing total price for first class to be used also in final Total
def totalPrice(result):
    sum = 0
    for x in result:
        sum += x[6]
    return sum

print()

def printTable(resultList, bookingClass, average, total):
    print(f'{"="*20}{bookingClass:^25}{"="*20}')    #66 spaces
    print()
    print('-'*65)
    print(f'|{"Surname":^15}|{"FirstName":^15}|{"Price":^15}|{"Status":^15}|')
    print('-'*65)
    for x in resultList:
        print(f'|{x[1]:^15}|{x[2]:^15}|{x[6]:>15,.2f}|{x[9]:^15}|') #1.) format of the columns; 2.) selection of the columns
    print('-'*65, end="\n"*2)
    print(f"{bookingClass} Average Booking Price: {average:,.2f}")  #integer to string
    print(f"{bookingClass} Total Booking Revenue: {total:,.2f}")
    print(f"{bookingClass} Total Passengers: {len(resultList)}", end="\n"*2)
    print('='*65, end="\n"*2)

# Main code calling the defined functions

firstClassNumber, businessClassNumber, economyClassNumber = ticketInput()

classList = getDataFromDatabase()

FCresult = []
FilterFirstClass(classList, FCresult, firstClassNumber)
# Filtering the Business Class list
BCresult = []

FilterBusinessClass(classList, BCresult, businessClassNumber)
# Filtering the Economy Class list
ECresult = []
FilterEconomyClass(classList, ECresult, economyClassNumber)

printTable(FCresult, "First Class", averagePrice(FCresult), totalPrice(FCresult))
printTable(BCresult, "Business Class", averagePrice(BCresult), totalPrice(BCresult))
printTable(ECresult, "Economy Class", averagePrice(ECresult), totalPrice(ECresult))
print("="*65, end="\n"*2)
grandBookingTotalPrice = (totalPrice(FCresult) + totalPrice(BCresult) + totalPrice(ECresult))
print(f"Grand Total Booking Revenue: {grandBookingTotalPrice}", end="\n"*2)
print("="*65, end="\n"*2)
