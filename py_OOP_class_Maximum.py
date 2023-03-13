# OOP
# my fist class that give you which number is bigger
class Maximum:

    def __init__(self, x, y):
        print("Max of 2 values: ")
        self.x = x
        self.y = y
        if self.x > self.y:
            print(f"{self.x} > {self.y}")
        elif self.x == self.y:
            print(f"{self.x} = {self.y}")
        else:
            print(f"{self.y} > {self.x} ")


res = Maximum(1000, 1000)  # my class
