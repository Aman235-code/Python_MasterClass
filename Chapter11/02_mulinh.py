class Employee:
    company = "ITC"
    name = "Defaul Name"
    def show(self):
        print(f"{self.name} and {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"{self.language}")

class Programmer(Employee,Coder):
    company = "ITC Infotech"
    def showLang(self):
        print(f"{self.company} amd {self.language}")

a = Employee()
b = Programmer()
b.show()
b.showLang()
b.printLanguages()