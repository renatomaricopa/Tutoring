#!/usr/bin/env python3
"""This script contains functions to exercise dictionary concepts.
Author:
Date:
"""

# A dictionary is a bunch of key, value pairs
dictionary = {"name": "Jack", "age": "19"}


def dict_equal(dict1, dict2
    if len(dict1) != len(dict2):
        return False
    for key, value in dict1.items():
        if key not in dict2:
            return False
        elif key in dict2:
            if dict1[key] != dict2[key]:
                return False
    return True

answer = dict_equal({"name1": "Alice", "name2": "Bob"}, {"name1": "Alice", "name2": "Bob" })
print(answer)
# = True

"""
Examples:
dict_equal({"name1": "Alice", "name2": "Bob"}, {"name2": "Bob", "name1": "Alice"}) = True
dict_equal({}, {}) = True
dict_equal({"Name1": "Alice", "Name2": "Bob"}, {"name2": "Bob", "name1": "Alice"}) = False
dict_equal({"fruit": "banana"}, {"fruit": "banana", "meat": "beef"}) = False
"""

def count_words(sentence):
    dictionary = {}
    word_list = sentence.split(" ")
    word_list = list(map(lambda word: word.lower(), word_list))
    for word in word_list:
        if "," in word:
            word.replace(",","")
        if "." in word:
            word.replace(".","")
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] = dictionary[word] + 1
    return dictionary 
    
dictionary = count_words("The good the bad and the ugly") 
print(dictionary)
# = {"the": 3, "good": 1, "bad": 1, "and": 1, "ugly": 1}
    
"""
Examples:
count_words("The good the bad and the ugly") = {"the": 3, "good": 1, "bad": 1, "and": 1, "ugly": 1}
count_words("One fish, two fishes, red fish, blue fish") = {"one": 1, "fish": 3, "two": 1, "fishes": 1, "red": 1, "blue": 1}
count_words("One and one, two and two.") = {"one": 2, "and": 2, "two": 2}
"""

def morse(sentence):
    """morse returns a string with a morse translation of sentence.
    Morse code uses dots and dashes to represent letters.  Add one
    space between letters in a word, and a slash surrounded by two
    spaces between words.  You can assume that the string sentence
    will only have letters and spaces.  Notice that we have provided a
    dictionary named 'code' to help you.

    Examples:
    morse("hello") = ".... . .-.. .-.. ---"
    morse("World") = ".-- --- .-. .-.. -.."
    morse("Hello World") = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
    morse("SOS") = "... --- ..."
    """
    code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        }