from functools import reduce
# accumulate into one value

# def add(a, b):
#   return a+b

def add_all(lst):
  return reduce(lambda a,b: a+b, lst)

print(add_all([1,2,3,4,-5,6]))


def poly_eval(p, x):
  # add all polynomial parts together
  def add(a,b):
    return a+b
  # multiply coefficient by (x**i)
  def mult(a,b):
    return a*b
  # return value of x to the ith power
  def x_powers(i):
  	return x**i  
      
  x_list = map(x_powers, range(0, len(p))) 
  coef_x_list = map(mult, x_list, p)
  return reduce(add, coef_x_list)

print(poly_eval([1,2,3], 2))