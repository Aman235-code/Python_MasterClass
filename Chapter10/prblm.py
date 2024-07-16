# class Programmer:
#     company = "Microsoft"

#     def __init__(self,name,salary,pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin 


# p = Programmer("Aman",120000, 675888)
# print(p.name, p.salary, p.pin, p.company)
# r = Programmer("Rohan",65444,68775)
# print(r.name, r.salary, r.pin, r.company)

# class Calculator:
#     def __init__(self,n):
#         self.n = n 

#     def square(self):
#         print(f"{self.n*self.n}")

#     def cube(self):
#         print(f"{self.n*self.n*self.n}")

#     def squareRoot(self):
#         print(f"{self.n**1/2}")

#     @staticmethod
#     def hello():
#         print("hello there")


# a = Calculator(64)
# a.hello()
# a.square()
# a.cube()
# a.squareRoot()


# class Demo:
#     a = 5

# o = Demo()
# print(o.a)
# o.a = 0
# print(o.a)
# print(Demo.a)

from random import randint
class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to} ")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running successfully on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)} ")

t = Train(12399)
t.book("Rampur","Delhi")
t.getStatus()

t.getFare("Rampur","Delhi")

