# Lambda is an anonymous function

list1 = [1,2,3,4,5]

# def addOne(alist):
#     for i in range(len(alist)):
#         alist[i] += 1 
# def addOne(x):
#     return x+1 


newList = list(map(lambda x: x+1, list1))
print(newList)

list2 = [[3, "banana"], [4, "apple"], [2, "dog"]]
list2.sort(key=lambda x: x[1])
print(list2)

# print(newList)
newList = list(filter(lambda x: x == 2, newList))
print(newList)

# list comprehension
list2 = [1,2,3,4,5]
# for i in range(len(list2)):
#     if list2[i] == 2:
#         list2[i] = list2[i] * 3
# print(list2)

list2 = [list2[i]*3 if list2[i] == 2 else list2[i] for i in range(len(list2))]
print(list2)