# my Calculator
class Calcularor:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y
    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def div(self):
        return self.x / self.y

z = Calcularor(4,5)
print(z.sum())
print(z.sub())
print(z.mul())
print(z.div())
