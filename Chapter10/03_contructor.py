class Employee:
    language = "py"
    salary  = 1200000

    def __init__(self,name,salary,language): # dunder method automatically called
        self.name = name 
        self.salary = salary
        self.language = language
        print("Creating an obj")

    def getInfo(self):
        print(f"{self.language} and {self.salary}")

    @staticmethod # no passing the object 
    def greet():
        print("Good")

aman = Employee("Aman",1300000,"JS")
# aman.name = "Aman"
print(aman.name,aman.salary,aman.language)
aman.getInfo()

# rohan = Employee()


