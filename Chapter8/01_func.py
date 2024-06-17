# a = 12
# b = 45
# c = 67

# avg = (a+b+c)/3
# print(avg)

def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))
    avge = (a+b+c)/3
    print(avge)

# avg()
def goodDay(name):
    print(f"Good Day {name}")
    return "Done"
# a = goodDay("Aman")
# print(a)

def goodDay(name,ending="Thank You"):
    print(f"Good Day, {name}")
    print(ending)

# goodDay("Aman")
# goodDay("Ayan","Thanks")

