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
first_name = artist["first"]
last_name = artist["last"]
name = first_name + " " + last_name
name = f"{first_name} {last_name}"
print(name)
# Assignment 3 (BONUS)
# Another way to define a dictionary where the key is ALWAYS a string. (Same way you create variables)
# loop through this dictionary and add up all the donations
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# people = ["Shwetha", "Tim"]
# for person in people:
#     print(person)

# i = 0
# for pair in donations.items():
#     if i % 2 == 0:
#         print(pair)
#     i += 1
# for key, value in donations.items(): # returns a tuple (an immutable list of 2 values)
#     print(key, value)

# for key in donations.keys(): # return us the keys
#     print(key)
# for values in donations.values(): # returns us the values
#     print(values)
sumValues = 0
for values in donations.values():
    sumValues += values
print(sumValues)

donations2 = donations.copy()
print(donations2)

donations.pop("sam")
donations["lena"] = 2323
print(donations)

for key, value in donations.items():
    if key == "chuck":
        donations[key] = [value, 20.0]
print(donations)

for key, value in donations.items():
    if key == "chuck":
        value.append(33)
        donations[key] = value
print(donations)
'''
# Create an empty dictionary called profile. Add your name, age, and favorite color
# Create another dictionary called profile2 by making a copy of the previous one.
    # Grab user input by asking them what their name, age, and favorite color is.
    # Update the values in profile2 with the user input.
    # print out a string that says, for example: "My name is Timothy, I am 20, and my favorite color is green".
    # Finally, remove all of the values in profile2 using a LOOP and pop()
'''
profile = {}
profile["name"] = "Shwetha"
profile["age"] = 13
profile["favorite color"] = "yellow"

print(profile)

profile2 = profile.copy()

print(profile2)

name = input("Enter name: ")
age = input("Enter age: ")
color = input("Enter favorite color: ")

profile2["name"] = name
profile2["age"] = age
profile2["favorite color"] = color

print(profile2)

sentence = f"My name is {name}, I am {age}, and my favorite color is {color}"
print(sentence)
copy_profile2 = profile2.copy()
for values in copy_profile2:
    profile2.pop(values)

print(profile2)


# Homework/Challenge
# Go through the playlist, loop through the songs in the playlist, and add up the duration. Print total duration.
playlist = {
	'title': 'patagonia bus',
	'author': 'colt steele',
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

total_duration = 0


