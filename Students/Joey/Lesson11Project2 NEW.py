"""
Program: Lesson10Project2_JOE2813225
Author: Joey Patrick
Last date modified: 7/24/2021

The purpose of this program is to modify our restaurant project to include
threads and a log file of actions that take place within the module.
"""

#Define the Arizona state sales tax rate.
arizonaTaxRate = 1.056

#Import the system, threading, breezypython, tkinter, and logging modules.
import sys
from threading import Thread
from breezypythongui import EasyFrame
from tkinter import *
import time
import logging
#Format the basic configuration of the log file.
logging.basicConfig(filename = 'restaurantLog.log', encoding = 'utf-8', level = logging.DEBUG, format='%(levelname)s: %(asctime)s: %(message)s')

#Define a MyThread class that takes in a certain level of importance and a message.
class MyThread(Thread):
    #In the init method, define the level and message variables.
    def __init__(self, level, message):
        self.level = level
        self.message = message
        Thread.__init__(self, name = "loggingThread")
    #In the run method, define the four different levels in order of importance.
    def run(self):
        if self.level == 1:
            logging.debug(self.message)
        if self.level == 2:
            logging.info(self.message)
        if self.level == 3:
            logging.critical(self.message)
        if self.level == 4:
            logging.error(self.message)
            
#Define MenuItem class to include the item name, retail and wholesale prices, number of sales, and a brief description of each menu item.
class MenuItem(object):
    #In the init method, define the necessary variables that are a part of each menu item.
    def __init__(self, itemName, retailPrice, wholesalePrice, sales, description):
        self.itemName = itemName
        self.retailPrice = retailPrice
        self.wholesalePrice = wholesalePrice
        self.sales = sales
        self.description = description
    #Define a module that returns all the information about an item for the manager.
    def returnManagerInfo(self):
        return(f"{self.itemName}, ${self.retailPrice:.2f}, ${self.wholesalePrice:.2f}, {self.sales}, {self.description}")
    #Define another module that only returns info pertinent to the customer: name, retail price, and description.
    def returnCustomerInfo(self):
        return(f"{self.itemName}, ${self.retailPrice:.2f}, {self.description}")

#Customer Class
class Customer(object):
    def __init__(self, customerName, vehicle):
        self.customerName = customerName
        self.vehicle = vehicle
        self.checkInTime = 0
    def setTime(self):
        obj = time.localtime()
        self.checkInTime = time.asctime(obj)
        return self.checkInTime
    def returnCustomerCheckIn(self):
        return(self.customerName + ", " + self.vehicle)
    def returnParkingLotCheckIn(self):
        return(self.customerName + ", " + self.vehicle + ", " + self.setTime())
    
    #strftime("%a, %d %b %Y, %H:%M:%S")

#Define an Order class that includes modules for adding and removing items, increasing sales, and getting a total price.
class Order(object):
    #In the init method, create a blank list for the customer's order, and log the fact that a new order was created.
    def __init__(self):
        self.order = []
        newThread = MyThread(1, "New Order Created\n")
        newThread.start()
    #Define a method that adds menu items to the order list and logs which items were added to the order.
    def addItems(self, menuItem):
        self.order.append(menuItem)
        newThread = MyThread(1, "This Item was added to the customer order: " + menuItem.returnManagerInfo())
        newThread.start()
    #Define a method that removes menu items from the order list and logs which items were removed from the order.
    def removeItems(self, index):
        try:
            removedItem = self.order.pop(index)
            newThread = MyThread(1, "This Item was removed from the customer order: " + removedItem.returnManagerInfo())
            newThread.start()
        except:
            newThread = MyThread(4, "ERROR with removing items:" + str(index))
            newThread.start()
    #Define a method that increases the number of sales for each item each time they are ordered.
    def increaseSales(self):
        for i in range(len(self.order)):
            self.order[i].sales += 1
    #Define a method that returns the subtotal of the order and logs the order's subtotal.
    def getTotal(self, tipPercentage):
        totalPrice = 0
        for i in range(len(self.order)):
            totalPrice += self.order[i].retailPrice
        newThread = MyThread(1, f"This is the subtotal of the order: ${totalPrice:.2f}\n")
        newThread.start()
        return Total(totalPrice, tipPercentage)
    
#Define a Total class that includes modules for calculating the tax, tip, and grand total.   
class Total(object):
    #In the init method, use the subtotal generated in getTotal above, and use the tipPercentage entered below.
    #Also log the fact that the customer placed the order.
    def __init__(self, subTotal, tipPercentage):
        newThread = MyThread(1, "Customer Placed the Order.\n")
        newThread.start()
        self.subTotal = subTotal
        self.tipPercentage = tipPercentage
    #Define a method that calculates the amount of tax.
    def taxCalculation(self):
        return self.subTotal*(arizonaTaxRate - 1)
    #Define a method that calculates the amount of tip.
    def tipCalculation(self):
        return self.subTotal*(self.tipPercentage/100)
    #Define a method that calculates the grand total.
    def grandTotalCalculation(self):
        return self.subTotal + self.taxCalculation() + self.tipCalculation()

#Open and read the Midterm Project Menu text file.
f = open("Midterm Project Menu.txt", 'r')

#Split text file by lines, add each line to the items list.
menu = []
for line in f:
    temp = line.split(", ")
    itemName = temp[0]
    retailPrice = float(temp[1][1:])
    wholesalePrice = float(temp[2][1:])
    sales = int(temp[3])
    description = temp[4]
    #Define the menuItem variable using the MenuItem class and the variables above.
    menuItem = MenuItem(itemName, retailPrice, wholesalePrice, sales, description)
    #Add each menuItem to the menu list.
    menu.append(menuItem)   
f.close()

#Define the Restaurant Module Class with EasyFrame.
class RestaurantModule(EasyFrame):
    def __init__(self):
        #Create the basic frame of the initial main menu.    
        EasyFrame.__init__(self, title = "Restaurant Module Main Menu")
        greeting = "Welcome! Please select an option below:"
        self.hintLabel = self.addLabel(text = greeting, row = 0, column = 0, sticky = "NSEW", columnspan = 3)
        #Create manager, customer, and exit buttons that comprise the main menu and use the functions defined above.
        self.managerButton = self.addButton(text = "Manager", row = 1, column = 0, command = self.manager)
        self.customerButton = self.addButton(text = "Customer", row = 1, column = 1, command = self.customer)
        self.valetButton = self.addButton(text = "Valet", row = 1, column = 2, command = self.valet)
        self.exitButton = self.addButton(text = "Exit", row = 1, column = 3, command = self.exit1)
        self.pressedButton = False
    #Define the manager function and a List Box class.
    def manager(self):
        class ListboxDemo(EasyFrame):
            def __init__(self, parent):
                EasyFrame.__init__(self, title = "Manager Portal")
                # Set up the list box with various parameters.
                self.listBox = self.addListbox(row = 1, column = 0, width = 90, rowspan = 4,
                                               listItemSelected = self.listItemSelected)
                #Add a label above the top of the List Box.
                self.addLabel(text = "Name, Retail Price, Wholesale Price, Sales", row = 0, column = 0)

                #Use a for loop to loop through the menu list and add each menu item to the list box.
                for menuItem in menu:
                    self.listBox.insert(END, menuItem.returnManagerInfo())
                self.listBox.setSelectedIndex(0)
                #Define self.parent so that the program can reference self.pressedButton, in the RestaurantModule class, later.
                self.parent = parent

                # Create more labels.
                self.addLabel(text = "Input", row = 1, column = 1)
                self.addLabel(text = "Index", row = 2, column = 1)
                self.addLabel(text = "Current item", row = 3, column = 1)
                self.addLabel(text = "Search by Sales", row = 5, column = 1)

                #Add text and integer fields.
                self.inputField = self.addTextField(text = "", row = 1,
                                                    column = 2, width = 40)
                self.indexField = self.addIntegerField(value = "", row = 2,
                                                       column = 2, width = 10)
                self.itemField = self.addTextField(text = "", row = 3,
                                                   column = 2, width = 40)
                self.searchSalesField = self.addIntegerField(value = "", row = 5,
                                                             column = 2, width = 40)
                #Add buttons
                self.addButton(text = "Add", row = 4,
                               column = 1, command = self.add)
                self.removeButton = self.addButton(text = "Remove", row = 4,
                                                   column = 2, command = self.remove)
                self.addButton(text = "Search", row = 6, column = 2,
                               command = self.search)
                self.addButton(text = "Return to Main Menu", row = 7, column = 2,
                               command = self.returnToMenu)

                # Display current index and currently selected item
                self.listItemSelected(0)

            #Now define an add function, which the Add Button will use to add new menu items to the listbox.
            def add(self):
                item = self.inputField.getText()
                #Use a series of if-else statements to define the actions of the function.
                if item != "":
                    newThread = MyThread(1, "New Menu Item Added by Manager: " + item + "\n")
                    newThread.start()
                    index = self.listBox.getSelectedIndex()
                    temp = item.split(", ")
                    itemName = temp[0]
                    retailPrice = float(temp[1][1:])
                    wholesalePrice = float(temp[2][1:])
                    sales = int(temp[3])
                    description = temp[4] + "\n"
                    menuItem = MenuItem(itemName, retailPrice, wholesalePrice, sales, description)  
                    if index == -1:
                        menu.insert(0, menuItem)
                        self.listBox.insert(0, menuItem.returnManagerInfo())
                        self.listBox.setSelectedIndex(0)
                        self.listItemSelected(0)
                        self.removeButton["state"] = NORMAL
                    else:
                        menu.insert(index, menuItem)
                        self.listBox.insert(index, menuItem.returnManagerInfo())
                        self.listItemSelected(index + 1)
                    self.inputField.setText("")

            #Define a remove function, which the Remove button will use to remove items from the listbox.
            def remove(self):
                index = self.listBox.getSelectedIndex()
                self.listBox.delete(index)
                itemRemoved = menu.pop(index)
                newThread = MyThread(1, "Menu Item Removed by Manager: " + itemRemoved.returnManagerInfo())
                newThread.start()
                #Again, use a series of if-else statements to define the actions of the function.
                if self.listBox.size() > 0:
                    if index > 0:
                        index -= 1
                    self.listBox.setSelectedIndex(index)
                    self.listItemSelected(index)
                else:
                    self.listItemSelected(-1)
                    self.removeButton["state"] = DISABLED

            #Define a search function, which the Search button will use to allow the manager to find all items below the sales target entered.
            def search(self):
                #Use a try-else statement to account for potential errors when entered.
                try:
                    message = ""
                    #Use a for loop to loop through the menu list, and add any items with a sales amount less than the number entered to the message.
                    for item in menu:
                        if item.sales <= self.searchSalesField.getNumber():
                            message += item.returnManagerInfo()
                            
                    if message == "": message = "No Sales Target Entered"
                    #Display the pop-up message box with all relevant items.
                    self.messageBox(title = "Search Results", message = message)
                    newThread = MyThread(1, "Items in Manager Search: \n" + message)
                    newThread.start()
                except ValueError:
                    self.messageBox(title = "ERROR",
                                    message = "Input must be an integer >= 0")

            #Define a returnToMenu function that closes the manager menu and resets self.pressedButton, in the restaurant module class, to False.
            def returnToMenu(self):
                self.destroy()
                self.parent.pressedButton = False
                
                        
            #Define the listItemSelected function so the program recognizes whichever item is selected by the user.
            def listItemSelected(self, index):
                self.indexField.setNumber(index)
                self.itemField.setText(self.listBox.getSelectedItem())
                
        #Allow the ListboxDemo class to loop and create another if statement to allow only one window to be open at a time.
        if self.pressedButton == False:
            self.pressedButton = True
            ListboxDemo(self).mainloop()
        
    #Now define the customer side of the interface, again using a list box class with EasyFrame.
    def customer(self):
        class ListboxDemo(EasyFrame):
            def __init__(self, parent):
                EasyFrame.__init__(self, title = "Customer Portal")
                # Set up the list box and an order, or cart, list box by adding their paramaters.
                self.listBox = self.addListbox(row = 1, column = 0, width = 80, rowspan = 4,
                                               listItemSelected = self.listItemSelected)
                self.Cart = self.addListbox(row = 6, column = 0, width = 80, rowspan = 4,
                                            listItemSelected = self.cartItemSelected)

                #Create another blank list for items to be added to later.
                self.order = Order()
                #Once again, define self.parent for later.
                self.parent = parent

                #Add a label above the menu list box.
                self.addLabel(text = "Name, Price", row = 0, column = 0)

                #Use a for loop to loop through the menu list and add each menu item to the list box.
                for menuItem in menu:
                    self.listBox.insert(END, menuItem.returnCustomerInfo())
                self.listBox.setSelectedIndex(0)

                #Add labels to the interface.
                self.addLabel(text = "Current item", row = 1, column = 1)
                self.addLabel(text = "Search Menu", row = 5, column = 1)
                self.addLabel(text = "Your Order", row = 5, column = 0)
                
                #Add text and integer fields.
                self.itemField = self.addTextField(text = "", row = 1, column = 2, width = 40)
                self.searchField = self.addIntegerField(value = "", row = 5, column = 2, width = 40)
                self.tipField = self.addIntegerField(value = "", row = 3, column = 2, width = 40)

                #Add buttons and add the functions they will need to use.
                self.addButton(text = "Add", row = 2,
                               column = 1, command = self.add)
                self.addTipButton = self.addButton(text = "Add Tip Percentage", row = 3, column = 1,
                                  command = self.addTip)
                self.removeButton = self.addButton(text = "Delete", row = 2,
                                                   column = 2, command = self.remove)
                self.placeOrderButton = self.addButton(text = "Place Order", row = 4,
                                                       column = 1, command = self.placeOrder)
                self.addButton(text = "Search", row = 6, column = 2,
                               command = self.searchMenu)
                self.addButton(text = "Return to Main Menu", row = 7, column = 2,
                               command = self.returnToMenu)
                self.tip = 0
                self.listItemSelected(0)
                
            #Define the add function that the add button will use so that the customer can add as many items as they like to their order listbox.
            def add(self):
                itemIndex = self.listBox.getSelectedIndex()
                selectedItem = menu[itemIndex]
                self.order.addItems(selectedItem)
                self.Cart.insert(END, selectedItem.returnCustomerInfo())

            #Define the remove function that the customer will use with the remove button to remove items from their order listbox.
            def remove(self):
                index = self.Cart.getSelectedIndex()
                self.Cart.delete(index)
                self.order.removeItems(index)
                if self.Cart.size() > 0:
                    if index > 0:
                        index -= 1
                    self.Cart.setSelectedIndex(index)
                    self.cartItemSelected(index)
                else:
                    self.cartItemSelected(-1)
            
            #Define the place order function that the place order button will use when the customer places their final order.
            def placeOrder(self):
                netTotal = self.order.getTotal(self.tip)
                taxCalc = netTotal.taxCalculation()
                tipCalc = netTotal.tipCalculation()
                grandTotalCalc = netTotal.grandTotalCalculation()
                #Log the tax amount for the order.
                newThread = MyThread(1, "Tax Amount Added: " + "${:,.2f}".format(taxCalc) + "\n")
                newThread.start()
                #Log the tip amount for the order.
                newThread2 = MyThread(1, "Tip Amount Added: " + "${:,.2f}".format(tipCalc) + "\n")
                newThread2.start()
                #Log the grand total of the order.
                newThread3 = MyThread(1, "Grand Total of the Order: " + "${:,.2f}".format(grandTotalCalc) + "\n")
                newThread3.start()
                
                #Create the message for the receipt pop-up message box that will appear when the customer presses the place order button.        
                message = f"Subtotal: ${netTotal.subTotal:.2f}\nTax Amount: ${taxCalc:.2f}\nTip Amount: ${tipCalc:.2f}\nGrand Total: ${grandTotalCalc:.2f}"
                self.messageBox(title = "Receipt", message = message)
                self.order.increaseSales()

            #Define the search menu function that will search the menu for anything with a partial match to what the user enters.
            def searchMenu(self):
                message = ""
                #Use another for loop to loop throught each menu item in the menu list.
                for item in menu:
                    #Use an if statement to add all items with a partial match to a search results pop-up window.
                    if self.searchField.getValue().lower() in item.itemName.lower():
                        message += item.returnCustomerInfo()

                #Create two more messages to assist the customer in refining their search.
                if self.searchField.getValue() == "": message = "No item entered!"
                if message == "": message = "Please search again using an item name."
                self.messageBox(title = "Search Results", message = message)
                #Log the items customers search for to see which items generate the most interest.
                newThread = MyThread(1, "Items in Customer Search: \n" + message)
                newThread.start()

            #Define the add tip function that will properly add a tip amount to the order using arithmetic.
            def addTip(self):
                self.tip = float(self.tipField.getValue())
                #Create another message box to inform the user that the tip was added.
                self.messageBox(title = "Tip Added", message = f"{self.tip}% tip added")

            #Define a returnToMenu function that closes the customer window and resets self.pressedButton, in the restaurant module class, to False.
            def returnToMenu(self):
                self.destroy()
                self.parent.pressedButton = False
                
            #Define the list item selected function so the program recognizes the item selected in the menu list box.       
            def listItemSelected(self, index):
                #Responds to the selection of an item in the list box and updates the fields with the current item and its index.
                self.itemField.setText(self.listBox.getSelectedItem())

            #Define the list item selected function so the program recognizes the item selected in the order list box.         
            def cartItemSelected(self, index):
                self.itemField.setText(self.listBox.getSelectedItem())
                      
        # Instantiate and pop up the window, and create another if statement to allow only one window to be open at a time.
        if self.pressedButton == False:
            self.pressedButton = True
            ListboxDemo(self).mainloop()

    def valet(self):
        class ListboxDemo(EasyFrame):
            def __init__(self, parent):
                EasyFrame.__init__(self, title = "Valet Portal")
                # Set up the list box and an order, or cart, list box by adding their paramaters.
                self.CustomerBox = self.addListbox(row = 1, column = 0, width = 60, rowspan = 4,
                                               listItemSelected = self.CustomerItemSelected)
                self.ParkingLot = self.addListbox(row = 6, column = 0, width = 60, rowspan = 4,
                                            listItemSelected = self.ParkingLotItemSelected)

                #Create another blank list for items to be added to later.
                self.customerList = []
                
                self.parkingLotList = []
                #Once again, define self.parent for later.
                self.parent = parent

                #Add a label above the customer list box.
                self.addLabel(text = "Customer Name, Vehicle", row = 0, column = 0)

                self.CustomerBox.setSelectedIndex(0)

                #Add labels to the interface.
                self.addLabel(text = "Current Customer", row = 1, column = 1)
                self.addLabel(text = "Search Customers", row = 6, column = 1)
                self.addLabel(text = "Parking Lot", row = 5, column = 0)
                
                #Add text and integer fields.
                self.CustomerField = self.addTextField(text = "", row = 1, column = 2, width = 40)
                self.searchField = self.addTextField(text = "", row = 6, column = 2, width = 40)
                #self.tipField = self.addIntegerField(value = "", row = 3, column = 2, width = 40)

                #Add buttons and add the functions they will need to use.
                self.addToLotButton = self.addButton(text = "Add to Parking Lot", row = 3,
                               column = 1, command = self.addToLot)
                self.addCustomerButton = self.addButton(text = "Add Customer", row = 2, column = 1,
                                  command = self.add)
                self.removeFromLotButton = self.addButton(text = "Remove from Parking Lot", row = 3,
                                                   column = 2, command = self.removeFromLot)
                self.removeCustomerButton = self.addButton(text = "Remove Customer", row = 2, column = 2,
                                                           command = self.remove)
                #self.placeOrderButton = self.addButton(text = "Place Order", row = 4,
                                                       #column = 1, command = self.placeOrder)
                self.addButton(text = "Sort by Last Name", row = 5, column = 1,
                               command = self.sortByLastName)
                self.addButton(text = "Sort by Check In Time", row = 5, column = 2,
                               command = self.sortByTime)
                self.addButton(text = "Search", row = 7, column = 2,
                               command = self.searchMenu)
                self.addButton(text = "Return to Main Menu", row = 8, column = 2,
                               command = self.returnToMenu)
                #self.tip = 0
                self.CustomerItemSelected(0)
                
            #Define the add function that the add button will use so that the customer can add as many items as they like to their order listbox.
            def addToLot(self):
                customerIndex = self.CustomerBox.getSelectedIndex()
                selectedItem = self.customerList[customerIndex]
                #self.parkingLotList.addselectedItem(selectedItem)
                self.ParkingLot.insert(END, selectedItem.returnParkingLotCheckIn())
                self.parkingLotList.append(selectedItem.returnParkingLotCheckIn())
                print(self.parkingLotList)

            #Define the remove function that the customer will use with the remove button to remove items from their order listbox.
            def remove(self):
                index = self.ParkingLot.getSelectedIndex()
                self.ParkingLot.delete(index)
                self.parkingLotList.removeItems(index)
                if self.ParkingLot.size() > 0:
                    if index > 0:
                        index -= 1
                    self.ParkingLot.setSelectedIndex(index)
                    self.ParkingLotItemSelected(index)
                else:
                    self.ParkingLotItemSelected(-1)

            def add(self):
                customer = self.CustomerField.getText()
                temp = customer.split(", ")
                customer = Customer(temp[0], temp[1])
                self.customerList.append(customer)  
                print(self.customerList)
                self.CustomerBox.insert(len(self.customerList)-1, customer.returnCustomerCheckIn())
                





                
                """item = self.inputField.getText()
                #Use a series of if-else statements to define the actions of the function.
                if item != "":
                    newThread = MyThread(1, "New Menu Item Added by Manager: " + item + "\n")
                    newThread.start()
                    index = self.listBox.getSelectedIndex()
                    temp = item.split(", ")
                    itemName = temp[0]
                    retailPrice = float(temp[1][1:])
                    wholesalePrice = float(temp[2][1:])
                    sales = int(temp[3])
                    description = temp[4] + "\n"
                    menuItem = MenuItem(itemName, retailPrice, wholesalePrice, sales, description)  
                    if index == -1:
                        menu.insert(0, menuItem)
                        self.listBox.insert(0, menuItem.returnManagerInfo())
                        self.listBox.setSelectedIndex(0)
                        self.listItemSelected(0)
                        self.removeButton["state"] = NORMAL
                    else:
                        menu.insert(index, menuItem)
                        self.listBox.insert(index, menuItem.returnManagerInfo())
                        self.listItemSelected(index + 1)
                    self.inputField.setText("")"""

            #Define a remove function, which the Remove button will use to remove items from the listbox.
            def removeFromLot(self):
                index = self.ParkingLot.getSelectedIndex()
                self.ParkingLot.delete(index)
                itemRemoved = menu.pop(index)
                newThread = MyThread(1, "Vehicle left Parking Lot: " + itemRemoved.returnParkingLotCheckIn())
                newThread.start()
                #Again, use a series of if-else statements to define the actions of the function.
                if self.ParkingLot.size() > 0:
                    if index > 0:
                        index -= 1
                    self.ParkingLot.setSelectedIndex(index)
                    self.ParkingLotItemSelected(index)
                else:
                    self.ParkingLotItemSelected(-1)
                    self.removeButton["state"] = DISABLED

            def sortByLastName(self):
                def getKey(e):
                    return e.customerName
                self.parkingLotList.sort(key = getKey)
                self.customerList.sort(key = getKey)

            def sortByTime(self):
                def getKey(e):
                    return e.checkInTime
                self.parkingLotList.sort(key = getKey)
            
            #Define the search menu function that will search the menu for anything with a partial match to what the user enters.
            def searchMenu(self):
                message = ""
                #Use another for loop to loop throught each menu item in the menu list.
                for item in menu:
                    #Use an if statement to add all items with a partial match to a search results pop-up window.
                    if self.searchField.getValue().lower() in item.itemName.lower():
                        message += item.returnCustomerInfo()
                #Create two more messages to assist the customer in refining their search.
                if self.searchField.getValue() == "": message = "No item entered!"
                if message == "": message = "Please search again using an item name."
                self.messageBox(title = "Search Results", message = message)
                #Log the items customers search for to see which items generate the most interest.
                newThread = MyThread(1, "Items in Customer Search: \n" + message)
                newThread.start()
      
            #Define a returnToMenu function that closes the customer window and resets self.pressedButton, in the restaurant module class, to False.
            def returnToMenu(self):
                self.destroy()
                self.parent.pressedButton = False
                
            #Define the list item selected function so the program recognizes the item selected in the menu list box.       
            def CustomerItemSelected(self, index):
                #Responds to the selection of an item in the list box and updates the fields with the current item and its index.
                self.CustomerField.setText(self.CustomerBox.getSelectedItem())

            #Define the list item selected function so the program recognizes the item selected in the order list box.         
            def ParkingLotItemSelected(self, index):
                self.ParkingLot.getSelectedItem()
                      
        #Instantiate and pop up the window, and create another if statement to allow only one window to be open at a time.
        if self.pressedButton == False:
            self.pressedButton = True
            ListboxDemo(self).mainloop()


    #Now define the exit function that will properly close the program and update the menu text file when the exit button is pressed.
    def exit1(self):
        f = open("Midterm Project Menu.txt", 'w')
        updateFile = ""
        for item in menu:
            updateFile += item.returnManagerInfo()
        f.write(updateFile)
        sys.exit()
        
#Define the main function so that the program operates properly.                    
def main():
    RestaurantModule().mainloop()
if __name__ == "__main__":
    main()
        

