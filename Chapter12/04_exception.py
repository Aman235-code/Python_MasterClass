try:
    a = int(input("Hey, enter a number: "))
    print(a)
except ValueError as v:
    print("Value")
    print(v)
except Exception as e:
    print(e)

print("Thank you")