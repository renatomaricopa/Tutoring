

a = 1
def hello():
    global a 
    a += 3
    return a
print(a)
print(hello())
print(a)