word_list = ["f-grapes", "a-monkey", "a-elephant", "m-paper", "m-pencil", "f-mango"]

fruits = []
for thing in word_list:
    if thing[0] == "f":
        fruit = thing[2:] # note: you don't need to create a variable here because it's only used once
        fruits.append(fruit)


fruits = [thing[2:] for things in word_list if thing[0] == "f"]

print(fruits)

# Assn 1
# create a variable called "answer"
# This is a new list that contains the first letter of each name in the list
# names = ["Elie", "Tim", "Matt"]
# answer = [name[0] for name in names]
# print(answer)
# # Assn 2
# # create a variable called "answers2"
# # This is a new list of all the even values
# numbers = [1,2,3,4,5,6]
#
# answers2 = [integer for integer in numbers if integer %2 == 0]
# print(answers2)

#answers = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
# range(0,10)
# List will be called "answers"
answers=[]
for _ in range(0,10): # is on the second loop
    mini_list = []
    for number in range(0,10): # finished
        mini_list.append(number)
    answers.append(mini_list)

answers = [[number for number in range(0,10)] for _ in range(0,10)]
print(answers)

# Dictionaries are another data structure
# Key: Value pairs.
# The key can be any object that is a primitive type: integers, floats, strings, and booleans
# The value can be anything
word_dictionary = {"apple": "a fruit that is red and juicy", "orange": "a fruit that is orange and juicy"}
definition = word_dictionary["apple"]
# Add something to dictionary
word_dictionary["Two"] = 2
# Update something in our dictionary
word_dictionary["apple"] = "a fruit that is red, yellow, or green and juicy"
print(word_dictionary)
# Loop through dictionary
for key, value in word_dictionary.items():
    print(key, value)

# Assignment 1
# Create a dictionary called "user_info" and add 3 key value pairs to it (up to you what you want to add)
# e.g. Key = "shirt_color", Value = "green" or Key = "age", Value = 30
user_info = {}
user_info["shirt_color"] = "green"
user_info["age"] = 30
print(user_info)
# Assignment 2
# Extract the first name and the last name from "artist" dictionary
# Create a string that looks like this: "Neil Young"
artist = {"first": "Neil", "last": "Young"}

# Assignment 3 (BONUS)
# Another way to define a dictionary where the key is ALWAYS a string. (Same way you create variables)
# loop through this dictionary and add up all the donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)


