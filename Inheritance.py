
class Person():    # Parent Class

    def __init__(self,name,aadhar,phone):
        self.name=name
        self.aadhar=aadhar
        self.phone=phone

    def displayDetails(self):
        print(self.name + "\n" + self.aadhar + "\n" + self.phone )

class Employee(Person):   # Child Class

    def __init__(self,name,aadhar,phone,salary,designation):
        self.salary=salary
        self.designation=designation

        Person.__init__(self,name,aadhar,phone)
    def printDetails(self):
        print("Name =", self.name)
        print("Aadhar =", self.aadhar)
        print("Phone =", self.phone)
        print("Salary =", self.salary)
        print("Designation =", self.designation)

x = Employee("Rajesh","8769869","9526674440","56789","manager")
x.printDetails() # Property Of Child class
x.displayDetails() # Property Of Parent class


y=Person("Anish","3535353","80809080")





