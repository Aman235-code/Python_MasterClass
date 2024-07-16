# a = 89
# def fun():
#     global a
#     a = 3
#     print(a)

# fun()
# print(a)

l = [5,3,6765,322]

# index = 0
# for item in l:
#     print(f"{index} and {item}")
#     index+=1

# for index,item in enumerate(l):
#     print(index, item)

myList = [1,2,3,5,7,9]
# squaredList = []
# for i in myList:
#     squaredList.append(i*i)
# print(squaredList)

squaredList = [i*i for i in myList]
print(squaredList)