class Students:
    def __init__(self, name, age , ID):
        self.name = name
        self.age = age
        self.ID = ID
        self.marks = []        # the list should be defind here
        print(f'The Student {self.name} is {self.age} years old and have ID: {self.ID}')
    def addNoten(self,Noten):  # Noten is here as add_number
        self.marks.append(Noten)

    def avr(self):             # just add a avarage (method)
        return sum(self.marks)/len(self.marks)

class Maxi(Students):
    def __init__(self, name, age , ID):
        super(Maxi , self).__init__( name, age , ID)   # inheritance of constructor
        self.praktiken = "Praktikum"



Ziad = Students('Ziad Bari', 27 , 537846)
Ziad.addNoten(40)
Ziad.addNoten(46)
Ziad.addNoten(45)
Ziad.addNoten(43)
print(f'Ziad Noten = {Ziad.marks}')
print(f'Ziad avarage = {Ziad.avr()}')

d = Maxi('Ziad Bari', 27 , 537846)
print(d.praktiken)