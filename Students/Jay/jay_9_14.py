# qwerty = ['bla1', ['bla2', 'bla3'],'bla4', 1,2,3,4,6,7,7,7,7,77,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,7]
# # for element in qwerty:
# #     if type(element) is not list:
# #         print(element)
# #     else:
# #         for element2 in element:
# #             print(element2)
# qwerty2 = ['bla5', 'bla6']
# print(len(qwerty))
# qwerty.insert(len(qwerty)-1, qwerty2)
# print(qwerty)

# Dictionaries are key value pairs
#learning_python = {"ages": [10, 8, 20, 90, 15, 56, 47, 43], "skill": [40, 35, 809, 67, 98, 444, 335, 345]}
# print(learning_python["ages"])
# print(learning_python["skill"])
#learning_python["color"] = ["red", "green", "blue"]
#print(learning_python)
#learning_python["color"] = ["green", "green", "green"]
#learning_python["color"][-1] = "blue"
#print(learning_python)
#learning_python.pop("skill")
#for key, value in learning_python.items():
#    print(key, value)
import random
inventory = {"relic": None, "gold": 0, "map": False}
while not inventory["relic"] or inventory["gold"] < 100 or not map:
    item = random.choice([10, True, 20, 30, 50, 100, "staff"])
    if type(item) is int:
        inventory["gold"] += item
    elif item == "staff":
        inventory["relic"] = "staff"
    else:
        inventory["map"] = True
    print(inventory)
print("You won!")