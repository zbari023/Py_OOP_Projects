class Car:  # class
    # property
    color = 'red'
    modell = 2018
    motor = 'Benzin'
    # Methods or functions
    def kilometerage(self,amount):
        self.amount = amount


print("Object 1 of class Car :")
c1 = Car()  # copy 1 / Object 1
c1.color = 'black'
print(c1.color)
c1.motor = 'Desil'
print(c1.motor)
c1.modell = 'Maybach 2023'
print(c1.modell)
