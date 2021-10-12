listA = []
for num in range(0,10000 + 1):
   # prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            listA.append(num)
print(listA)