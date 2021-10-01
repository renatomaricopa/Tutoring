
#tuples & sets?
certainties = ("life", "life", "death", ["hello", "panda"],"gravity")
uncertainties = ["area51", "unicorns"]
uncertainties.append("aliens")
uncertainties.append("lazer beams")
print(uncertainties)
certainties[3].append("aliens")

print(certainties)
print(certainties.count("life"))
print(certainties.index("gravity"))

d1 = {"a": "apple", "b": "banana"}
for element in certainties:
    if type(element) == str:
        print("*" + element + "*")
    elif type(element) == list:
        for element2 in element:
            print("*" + element2 + "*")

# TUPLES ARE IMMUTABLE AND ORDERED. THEY CANNOT CHANGE.
# LISTS ARE MUTABLE AND ORDERED. THEY CAN CHANGE.

# SETS ARE MUTABLE AND UNORDERED. THEY CAN CHANGE. THEY CONTAIN UNIQUE VALUES.
data = [0, 1, 2, 4, 4, 4, 1, 0, 3, 3, 3, 3, 3, 3, 3, 80, 80, 80, 90, 90, "True", "True"]
new_data = set(data)
new_data.add(12345678987654323456)
print(new_data)
new_data.remove(12345678987654323456)
print(new_data)

for element in new_data:
    print(element)

# SET MATH
classA = {"Matthew", "Helen", "Jay", "James", "William", "KC"}
classB = {"Jay", "Charlotte", "Hannah", "Angel", "KC", "William"}
classC = {"Jay", "Charlotte", "Hannah", "Tom", "Jerry"}
classZ = classA | classB | classC
classY = classA & classB & classC
print(classZ)
print(classY)