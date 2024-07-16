# class TDVector:
#     def __init__(self,i,j):
#         self.i = i 
#         self.j = j
#     def show(self):
#         print(f"{self.i}i + {self.j}j")

# class ThreeVector(TDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k

#     def show(self):
#         print(f"{self.i}i + {self.j}j + {self.k}k")

# a = TDVector(1,2)
# a.show()
# b = ThreeVector(5,2,3)
# b.show()

# class Animals:
#     pass 

# class Pets(Animals):
#     pass 

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow")
    
# d = Dog()
# d.bark()

# class Employee:
#     salary = 234
#     increment = 20

#     @property
#     def sal(self):
#         return (self.salary + self.salary * (self.increment/100))

#     @sal.setter
#     def sal(self,salary):
#         self.increment = ((salary/self.salary)-1) * 100

# e = Employee()
# print(e.sal)
# e.sal = 280.8
# print(e.increment)


# class Complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i 

#     def __add__(self,c2):
#         return Complex(self.r + c2.r, self.i + c2.i)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"

# c1 = Complex(1,2)
# c2 = Complex(3,4)
# print(c1 + c2)
