sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# SUPERFRAGILEXPIDOCIOUS

# Define your code below:
# len(sounds)
# range(0, 10, 2) # 0, 2, 4, 6, 8
# print(sounds)
# length = len(sounds)
# final_word = ""
# for index in range(0, length, 2):
#     part = sounds[index] # indexing into a list
#     part = part.upper()
#     final_word += part
#
# print(final_word)
#
# # lists are objects just like everything else in python. Which means we can call functions/methods on them.
# # Create a list called instructors
# # Add the following strings to the instructors list
#     # "Colt"
#     # "Blue"
#     # "Lisa"
# # Run the tests to make sure you've done this correctly!
# instructors =[]
# instructors.append("Colt")
# instructors.append("Blue")
# instructors.append("Lisa")
# instructors.append("Tim")
# print(instructors)
#
# instructors.insert(1, "Tim")
# instructors2 = ["Jim", "Bob", "Shwetha"]
# instructors.extend(instructors2) # adds to the end (just like append)
# instructors.append(instructors2)
# print(instructors)
#
# instructors.pop(-1) # uses the index
# # instructors.remove()
# print(instructors)
#
# # for instructor in instructors:
# #     if instructor == "Tim":
# #         instructors.remove("Tim")
# # print(instructors)
#
# instructors.sort()
# print(instructors)


# instructors =[]
# instructors.append("Colt")
# instructors.append("Blue")
# instructors.append("Lisa")
# # Remove the last value in the list
# instructors.pop(-1)
# print(instructors)
# # Remove the first value in the list
# instructors.pop(0)
# print(instructors)
# # Add the string "Done" to the beginning of the list
# # done = ["done"]
# # done.extend(instructors)
# instructors.insert(0, "done")
# print(instructors)

a = "Hello World"
hello = a[0:5]
print(hello)
hello = a[-1]
print(hello)
# range(0, length, 2)
l1 = ["Hello", "my", "name", "is", "Tim", "and", "I", "like", "to", "code"]
iLikeToCode= l1[::-1]
print(iLikeToCode)

# list comprehension