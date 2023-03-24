# a program that know if the number odd or even

class Checkoddoreven():
    def __init__(self,a):
        try:
            a = int(a)
            if (a % 2) == 0:  # the condition
                print(f'{a} is even')
            else:
                print(f'{a} is odd')
        except ValueError:
            print('Enter please a value number : ')


Checkoddoreven('rgag')            # my class




'''
a = int(input('a= '))
if (a%2) == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')
'''