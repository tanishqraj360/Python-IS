n=int(input('Enter range: '))
f=[]
f.append(1)
f.append(1)
for i in range(2,n):
    c=f[i-2]+f[i-1]
    f.append(c)
print(f) 