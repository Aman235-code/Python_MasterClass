class Employee:
    company = "ITC"
    def show(self):
        print(f"{self.name} and {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"{self.name} and {self.salary}")
#     def showLang(self):
#         print(f"{self.language}")

class Programmer(Employee):
    company = "ITC Infotech"
    def showLang(self):
        print(f"{self.language}")

a = Employee()
b = Programmer()
print(a.company, b.company)