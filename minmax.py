def min_max(arr):  # defines function and parameter
    # [1,2,3,4,5] #[1]
    min = 999999999  # initializes minimum
    max = -999999999  # initializes maximum
    if not arr:
        return ()
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min, max)

arr = [7, 8, 6, -5, 4]
print(min_max(arr))
    
    




