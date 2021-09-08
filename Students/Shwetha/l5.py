# word_list = ["f-grapes", "a-monkey", "a-elephant", "m-paper", "m-pencil", "f-mango"]
#
# fruits = []
# animals = []
# misc = []
#
# for thing in word_list:
#     word = thing[0]
#     if word == "f":
#         fruit = thing[2:] # note: you don't need to create a variable here because it's only used once
#         fruits.append(fruit)
#     else:
#         other = thing[2:]
#         misc.append(other)
#
# print(fruits)
# print(animals)
# print(misc)

# a = "apple"
# b = "banana"
# c = "cantelope"
# d = "dumpling"
a, b, c, d = "apple", "banana", "cantelope", "dumpling"
# swap things
a, b = b, a
# fruits = ['grapes', 'mango']
print("Before Swap:", fruits)
fruits[0], fruits[1] = fruits[1], fruits[0] # this will swap it in place (it won't create a new list)
print("After Swap:", fruits)

# List Comprehension: will condense filling an array into one line
l1 = [1,2,3,4]
l2 = []
l3 = []
for number in l1:
    if number % 2 == 0:
        number *= 2
    l2.append(number)
for number in l1:
    if number % 2 == 0:
        l3.append(number*2)
print(l2)
print(l3)
# List Comprehension Version of normal loop above
_l2 = [number*2 if number % 2 == 0 else number for number in l1]
_l3 = [number*2 for number in l1 if number % 2 == 0]
print(_l2)
print(_l3)

# HOMEWORK _______________________________
# Create a list using:
# 1. normal for loop
# 2. list comprehension version

word_list = ["f-grapes", "a-monkey", "a-elephant", "m-paper", "m-pencil", "f-mango"]

fruits = []
for thing in word_list:
    word = thing[0]
    if word == "f":
        fruit = thing[2:] # note: you don't need to create a variable here because it's only used once
        fruits.append(fruit)

