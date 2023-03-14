# Multiinheritance of more classes
class A:
    def do(self):
        print("you are in A")
class B(A):
    def do(self):
        print("you are in B")
class C:
    def do(self):
        print("you are in C")
class D(B,C):
    def do(self):
        print("you are in D")

c1 =  D()
print(c1.do())
print(D.mro())

# you are in D
# None
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]