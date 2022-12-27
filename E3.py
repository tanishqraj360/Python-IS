import statistics
l=[]
n=int(input('How many numbers do you want to enter: '))
for i in range(n):
    a=int(input('Enter number: '))
    l.append(a)
print(statistics.mean(l))
print(statistics.variance(l))
print(statistics.stdev(l))
