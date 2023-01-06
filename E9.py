class Complex():
    def __init__(self, a, b):
        self.a=a
        self.b=b
    
    def add(self):
        print(self.a+self.b)

n=int(input('Enter number: '))
if n>=2:
    for i in range(n):
        a=complex(input('Enter first complex number: '))
        b=complex(input('Enter second complex number: '))
        a1=Complex(a,b)
        a1.add()
else:
    print('Invalid input. Enter number greater than 2')
