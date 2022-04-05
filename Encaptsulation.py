
# Data Encapsulation

class Goverment:

    def __init__(self, price):
        self.__price = price

    def viewPetrolPrice(self):
        print(self.__price)

    def hikePrice(self,price):
        self.__price = price


centralGovt = Goverment(90)

centralGovt.viewPetrolPrice()

centralGovt.__price = 130    # Outside
centralGovt.viewPetrolPrice()

centralGovt.hikePrice(120)
centralGovt.viewPetrolPrice()












