class Employee:
    language = "py"
    salary  = 1200000

    def getInfo(self):
        print(f"{self.language} and {self.salary}")

    @staticmethod # no passing the object 
    def greet():
        print("Good")

aman = Employee()
aman.language = "JS"
aman.getInfo()
aman.greet()
# Employee.getInfo(aman)


