# Example class and OOP
class Student:
    def __init__(self,name,age,classroom):
        self.name = name
        self.age = age
        self.classroom = classroom
        print(f'The student {self.name} is {self.age} years old and he prisent in the Room number {self.classroom} ')
c1 = Student('Ziad Bari', 25 ,115)