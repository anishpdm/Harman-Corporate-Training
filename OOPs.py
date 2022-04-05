class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def printData(self):
        print(self.model)
        print(self.color)
        print(self.year)

    def getCustomer(self,name):
        self.name=name

    def printCustomer(self):
        print(self.name)

getModel=input("Enter Model ?")
getColor=input("Enter Color ?")
getYear=input("Enter Year ?")

bmw = Car(getModel, getColor, getYear)   #Object

bmw.getCustomer("Remya")
bmw.printCustomer()









