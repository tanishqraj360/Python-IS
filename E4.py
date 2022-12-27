a=str(input('Enter string: '))
l=['1','2','3','4','5','6','7','8','9','0']
for i in l:
    c=0
    for j in a:
        if i==j:
            c+=1
    print('Number of %s: '%(i),c)