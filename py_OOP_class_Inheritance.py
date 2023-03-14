class Calculator:
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
class ScieCal(Calculator):      # inheritance
    def pow(self):
        return self.x ** self.y
c1=ScieCal(12,3)
print(c1.sub())
print(c1.pow())