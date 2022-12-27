fname=input('Enter file directory/name: ')
d={}
with open(fname,'r') as f:
    content=f.read()
    word=content.split()

for i in word:
    k=i
    v=len(k)
    d[k]=v

sortd=sorted(d.items(), key=lambda x:x[1], reverse=True)
print(sortd[0:10])
