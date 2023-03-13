class Car:  # class
    # property or Attribute
    color = 'red'
    modell = 2018
    motor = 'Benzin'
    # Methods or functions
    def kilometerage(self,amount,limit):   # encapculation that placedholder for the object
        self.amount = amount
        self.limit = limit
        print(f"The Car drived {self.amount} and can go untel {self.limit}")

    def __init__(self):       # constructor, a special method that automatically called at the begin
        print("Welcome in this Automarkt :")



print("Object 1 of class Car :")
c1 = Car()  # copy 1 / Object 1
c1.color = 'black'
print(c1.color)
c1.motor = 'Desil'
print(c1.motor)
c1.modell = 'Maybach 2023'
print(c1.modell)

print("the output of function: ")
c1.kilometerage("127 km","200 km")

