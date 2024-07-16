# def square(n):
#     return n*n

square = lambda x : x*x
# print(square(5))

a = ["Aman","Rohan","Shubh"]
final = "::".join(a)
# print(final)

a = "{1} is a good {0}".format("harry", "boy") 
# print(a)

# Map 
# l = [1,2,3,4,5]
# square = lambda x: x*x 
# sqList = map(square, l)
# print(list(sqList))

# Filter 
# l = [1,2,3,4,5]
# def even(n):
#     if n%2 == 0:
#         return True 
#     return False 
# onlyeven = filter(even, l)
# print(list(onlyeven))

# Reduce
from functools import reduce
l = [1,2,3,4,5] 
def sum(a,b):
    return a + b 

mul = lambda x,y : x * y 
print(reduce(sum,l))
print(reduce(mul,l))

