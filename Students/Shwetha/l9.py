'''
'''

# def printName(first, last):
#     print(f"{first} {last}")
#
# printName("Timothy","Simanhadi")

def makeNoise():
    print("The crowd makes noise")

makeNoise()

# say_hi
# input: "Tim"
# output(return): "Hi Tim"

def sayHi(name):
    return("Hi " + name)

print(sayHi("Tim"))

#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

def generate_evens():
    evens = []
    for number in range(0, 51):
        if number % 2 == 0:
            evens.append(number)
    return evens

print(generate_evens())

# change_case
# this function, will take a string argument, and return the string in ALL CAPS
# e.g. "hello there" -> change_case() -> "HELLO THERE"

def change_case():
    first = "hello there"
    second = first.upper()
    return second
print(change_case())


# Without adding any new lines of code, make count_dollar_signs work as intended
# Return the number of "$" in the word.
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
print(count_dollar_signs("$uper $ize"))

# Create a function called "product" that takes the product of two numbers and returns the product

def product(first, second):
    return first * second

print(product(3, 4))

# Create a function called "last element" that takes a list and returns the last element in the list
l1 = ["a", "b", "c", "d"]
def last_element(myList):
    return myList[-1]

print(last_element(l1))

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''


# flesh out multiple_letter count:
def multiple_letter_count(word):
    frequency = {}
    for letter in word:
        if letter in frequency:
            frequency[letter] = frequency[letter] + 1
        else:
            frequency[letter] = 1
    return frequency
print(multiple_letter_count("hello"))