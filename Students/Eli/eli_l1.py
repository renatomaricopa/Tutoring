# Went over tic tac toe AI

# def findCrossoverIndexHelper(x, y, left, right):
#     if x[left] > y[left] and x[left+1] < y[left+1]: return left
#     else: return None
# def findCrossoverIndex(x, y):
#     n = len(x)
#     if len(x) != len(y): return None
#     else:
#         left = 0
#         right = n - 1
#         j = []
#         while (left <= right):
#             j.append(findCrossoverIndexHelper(x,y,left,right))
#             left += 1
#         return j

# x = [0,1,2,3,4,5,6,7]
# y = [-2,0,4,5,6,7,8,9]
# j1 = findCrossoverIndex(x, y)
# for i in j1:
#     if i != None:
#         j1 = i
# assert j1 == 1, "Test Case #1 Failed"

import functools
a = complex(1,2)
b = complex(2,4)
c = a+b
print(c.conjugate())

n = 123
s = 'hello'
b = b'n'
print(b)

sum_ = functools.reduce(lambda x,y: x+y,[2**x for x in range(11)])
print(1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512 + 1024)
print(sum_)