class Employee:
    a = 1
    @classmethod # 
    def show(cls):
        print(f"class attribute {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


    
e = Employee()
e.a = 45 
e.name  = "Aman Ahaed"
print(e.fname)
print(e.lname)
e.show()
