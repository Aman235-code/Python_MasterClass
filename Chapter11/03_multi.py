class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3 

o = Employee()
print(o.a)
p = Programmer()
print(p.a, p.b)
m = Manager()
print(m.a, m.b, m.c)