import random

a=random.randint(0,1000)
"""print(a)"""
t=0
x=int(input('Enter number: '))
while x!=a:

    t+=1
    if x>a:
        print('Number is greater.')
    else:
        print('Number is lesser')
    x=int(input("Enter number: "))
if x==a:
    print("Congratulations!. You won in",t,'tries.')
