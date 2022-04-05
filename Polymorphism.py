
# overriding


class Birds:

    def fly(self):
        print("All birds can FLY...")

class Pigeon(Birds):

    def fly(self):
        super().fly()
        print("Pigeons can FLY")


ob=Pigeon()
ob.fly()






