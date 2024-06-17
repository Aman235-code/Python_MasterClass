# n = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# n = int(input("Enter a number: "))
# i = 1
# while(i<11):
#     print(f"{n} * {i} = {n*i}")
#     i+=1

# n = int(input("Number: "))
# for i in range(2,n):
#     if(n%i == 0):
#         print("Not Prime")
#         break
# else:
#     print("Prime")

# i = 1
# sum = 0
# n = int(input("Number: "))
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

# prod = 1
# n = int(input("Number: "))
# for i in range(1,n+1):
#     prod = prod * i
# print(f"{prod}")

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("*"*(2*i-1),end="")
#     print("")

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     print("*"*i)
    # print("")

# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#     if(i==1 or i==n):
#         print("*"*n,end="")
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

n = int(input("Number: "))
for i in range(10, 0,-1):
    print(f"{n} x {i} = {n*i}")