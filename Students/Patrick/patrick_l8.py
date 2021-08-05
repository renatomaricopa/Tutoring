# import random

# def convertPhrase(phrase):
#     hint = ""
#     for character in phrase:
#         if character != " ":
#             hint += "*"
#         else:
#             hint += " "
#     return hint

# def revise(hint,guess,phrase):
#     phrase = list(phrase)
#     hint = list(hint)
#     for index, letter in enumerate(phrase):
#         if guess.upper() == letter.upper():
#             hint[index] = phrase[index]
#     hint = "".join(hint)
#     return hint

# def main():
#     phrase_list = ["Hello World", "Goodbye", "Gotta Run"]  #establish a phrase. modify this so that a phrase is chosen from a list
#     phrase = random.choice(phrase_list) # randomly pick a phrase from our phrase list
#     hint = convertPhrase(phrase)    #write this function to get the hint for this phrase
#     missed_letters_count = 0
#     guessed_letters = []
#     while "*" in hint and missed_letters_count < 6:     # adjust to while still more to guess or 6 missed letters
#         print(hint)
#         guess = input("Guess a letter: ")
#         if guess not in guessed_letters:
#             guessed_letters.append(guess)
        
#             if guess.upper() in phrase.upper():    #case insensitive search
#                 # arguments: "***** *****", "o", "Hello World"
#                 hint = revise(hint,guess,phrase)   #write the revise function
#             else:
#                 missed_letters_count += 1
#                 print(guess, "is an incorrect guess.")  
#         else:
#             print("This letter has already been guessed. Choose a new letter.")
#     if "*" not in hint:
#         print("Phrase has been guessed")   # or were 6 misses the reason the loop ended?
#     else:
#         print("Sorry, you used all 6 of your guesses. You lose.")

# main()


# from random import randint

# def filllist(dicelist):
#     for count in range(5):
#         die = randint(1,6)
#         dicelist.append(die)
#     return

# def showlist(dicelist):
#     print("You rolled: ", end="")
#     for die in dicelist:
#         print(die, " ", end="")
#     print()
#     print()

# def yatzee(dicelist):
#     total = 0
#     dicelist = [6,6,6,6,6]
#     rollvalue = dicelist[0]

#     if dicelist.count(rollvalue) == 5:
#         total = 50
#     return total

# def chance(dicelist):
#     total = sum(dicelist)
#     return total

# def twos(dicelist):
#     number2s = dicelist.count(2)
#     total = number2s * 2
#     return total

# def sixes(dicelist):
#     number6s = dicelist.count(6)
#     total = number6s * 6
#     return total

# def four_of_kind(dicelist):
#     # [3,3,3,3,1]
#     dicelist = sorted(dicelist)
#     if dicelist[0] == dicelist[3] or dicelist[1] == dicelist[4]:
#         return sum(dicelist)
#     return 0

# def sequence_of_five(dicelist):
#     dicelist = sorted(dicelist)
#     if dicelist == [2,3,4,5,6] or dicelist == [1,2,3,4,5]:
#         return 40
#     return 0

# def main():
#     done = False
#     while not done:
#         dicelist = []
#         filllist(dicelist)
#         showlist(dicelist)
#         points = yatzee(dicelist)
#         format_string = "%-20s%5d\n"
#         print(format_string % ("Yatzee", points))

#         points = twos(dicelist)
#         print(format_string % ("2's", points))

#         points = sixes(dicelist)
#         print(format_string % ("6's", points))

#         points = four_of_kind(dicelist)
#         print(format_string % ("Four of a kind", points))

#         points = sequence_of_five(dicelist)
#         print(format_string % ("Sequence of five", points))

#         answer = input("roll again? Y or N: ")
#         if answer != "Y" and answer !="y":
#             dont = True
#         else:
#             print()

# main()


# 1. poession_list = []
# 2. item_list = ["Keys", "Gold", "Map", "Monkey"]
# 3. user_choice = input("TAKE or DROP an item") # make sure that they use the write word: "TAKE" or "DROP". Also make sure their second word exists. Also make sure that it is length 2 after splitting.
# 4. TAKE will grab an item from item_list and put it in their posession_list. DROP will grab an item from the posession list and drop it into the item_list.
# 5. If the action was successful, print out that it was.

# 1. get_command() #split up the user input and return take, drop, and the item if valid. Error checking.
# 2. take() # take the item from the item_list, put into posession_list, and remove it from item_list. Print that it was successful.
# 3. drop() # take the item from the possession_list, put into item_list, and remove it from posession_list. Print that it was successful.
# 4. display() display the current posession and item lists.

def display(posessions, items):
    if posessions:
        print("Posessions: ", posessions)
    else:
        print("You have no posessions!")
    if items:
        print("Items in Room: ", items)
    else:
        print("No more items in room")

def get_command(posessions, items):
    while True:
        user_input = input("Enter \"TAKE\" or \"DROP\" followed by the item you want: ")
        user_input = user_input.split(" ")
        if len(user_input) != 2:
            print("Error: Too many/too few arguments") 
        else:
            if user_input[0].upper() == "TAKE":
                if user_input[1].lower() in items:
                    return user_input[0].upper(), user_input[1].lower()
                else:
                    print("Error: Item is either invalid or has already been taken.")
            elif user_input[0].upper() == "DROP":
                if user_input[1].lower() in posessions:
                    return user_input[0].upper(), user_input[1].lower()
                else:
                    print("Error: Item is either invalid or has already been dropped.")
            else:
                print("Error: Please enter a valid command (\"TAKE\" or \"DROP\")")

def take(posessions, items, item):
    for i in items:
        if i == item:
            items.remove(i)
            break
    posessions.append(item)  

def drop(posessions, items, item):
    for i in posessions:
        if i == item:
            posessions.remove(i)
            break
    items.append(item)

def main():
    posession_list = []
    item_list = ["keys", "gold", "map", "monkey"]
    while True:
        display(posession_list, item_list)
        command, item = get_command(posession_list, item_list)
        if command == "TAKE":
            take(posession_list, item_list, item)
        else:
            drop(posession_list, item_list, item)

main()