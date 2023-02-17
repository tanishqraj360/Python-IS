fname=input('Enter file directory/name: ')
c=[]
d={}
with open(fname,'r') as f:
    content=f.read()
    word=content.split()

for i in word:
    c.append(i)

for i in c:
    count=0
    for j in c:
        if i==j:
            count+=1
    d[i]=count

sortd=sorted(d.items(), key=lambda x:x[1], reverse=True)
print(sortd[0:10])