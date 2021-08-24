# https://www.geeksforgeeks.org/pass-by-reference-vs-value-in-python/


# Python uses "pass by object reference"
def set_list(alist): # "alist" is the function variable
    alist.append("A") # this will add "X" to the list object that the variables "alist" and "mylist" point to (currently the same object)
    alist = ["A"] # this will reassign the variable "alist" to point to something else. "mylist" does not get reassigned. It is its own variable.
    return alist

mylist = ["X"] # "mylist" is the caller variable

set_list(mylist) 
print(mylist)
 
def set_str(string):
    string = string + "hello" # reassigns variable "string" to point to string + "hello" instead of the original object pointed to by both "string" and "mystring"
    return string

mystring = "hello" 
set_str(mystring)
print(mystring)