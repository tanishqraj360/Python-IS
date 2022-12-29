def DivExp(a,b):
    if b==0:
        print('Error. Integer Overflow')
    else:
        c=a/b
        return c

a=int(input('Enter first integer: '))
b=int(input('Enter second integer: '))

print(DivExp(a,b))
