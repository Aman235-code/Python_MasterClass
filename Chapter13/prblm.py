# name = input("Enter name: ")
# marks = int(input("Enter marks: "))
# phno = int(input("Phone number: "))

# s = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phno)
# print(s)

# table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)
# print(s)

# def div(n):
#     if n%5 == 0:
#         return True
#     return False

# a = [10,1,2,3,5525,764,8653,11,557,3,67]
# f = list(filter(div,a))
# print(f)

a = [1,2,3,4,5,6,7,8,9,10]
def greater(a,b):
    if a>b:
        return a
    else: 
        return b 
from functools import reduce
print(reduce(greater,a))
















