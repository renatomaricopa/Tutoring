# most functions have arguments.
# in the function definition, the name variable is the parameter. In the function call, it is called an argument.
def hello_name(name, food):
    if food == "wine":
        answer = input("Hello {}! Do you like wine?".format(name))
    print("goodbye")
    return answer

def multiply(number):
    return number * number * 2 * 492003891839

x = multiply(4)
print(x)
# calling/invoking function
# to do this, get the name of the function: "hello", and put "()" in front of it.
# n = "Steven"
# f = "wine"
# x = hello_name("Steven", f)	
# print(x)