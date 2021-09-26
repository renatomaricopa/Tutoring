
# Homework/Challenge
# Go through the playlist, loop through the songs in the playlist, and add up the duration. Print total duration
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
song_list = playlist['songs']
for song in song_list:
    total_duration += song['duration']

print(total_duration)


l1 = [1,2,3,4,5,6]
l2 = []
for i, num in enumerate(l1):
    if (num%2) == 0:
        l2.append(num)
# print(l2)

l2 = [num for i, num in enumerate(l1) if (num%2) == 0]
print(l2)

d1 = {"apple": 2, "bananas": 4, "grapes": 3}
d2 = {}
for key, value in d1.items():
    if value%2 == 0:
        d2[key] = value
print(d2)

d2 = {key:value for key, value in d1.items() if value%2 == 0}
print(d2)

# I want you to print a list of all the values in our d1 dictionary that are odd using LIST COMPREHENSION
d2 = [value for value in d1.values() if value%2 != 0]
print(d2)

playlist = {
	'title': 'patagonia bus',
	'author': 'colt steele',
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}
artist_list = []
# to add a list to another list use the .extend() method. e.g. artist_list.extend(['blue'])

songList = playlist['songs']
for songDictionary in songList:
    artist_list.extend(songDictionary['artist'])
print(artist_list)

songDictionary = {'title': 'song1', 'artist': ['blue'], 'duration': 2.5}
print(songDictionary['artist'])

# nested list (list of lists AKA 2d array/list)
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
# person_dictionary = {}
# for key,value in person:
#     person_dictionary[key] = value
# print(person_dictionary)
person_dictionary = {key: value for key, value in person}
print(person_dictionary)


# l1 = ['a','b','c']
# enumerate = ((0,'a'), (1, 'b'), (2, 'c'))
# for index, value in enumerate(l1):


# HOMEWORK 1:
vowels_list = ['a','e','i','o','u']
# Create a dictionary where it looks like the keys are the vowels and the value is 0 (for each key).
# I want you to do this using the non-dictionary comprehension way and the dictionary comprehension way.
# e.g. {"a": 0, "e": 0, ....}

# HOMEWORK 2:
# ASCII: A way to represent characters in decimal. For example, the capital letter 'A' can be represented with the ASCII value of 65
# https://www.asciitable.com/
# The letters 'A-Z' are represented using the ASCII code numbers: 65-90.
# How do I get the ASCII value associated with an ASCII code number? chr(65)
# Create a dictionary that looks like: {65: 'A', 66: 'B', ... 90: 'Z'}
print(chr(65))