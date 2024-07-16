a = int(input("Enter a Number 1: "))
b = int(input("Enter a Number 2: "))

if b == 0:
    raise ZeroDivisionError("Not meant to divide numbers by 0")
else:
    print(a/b)