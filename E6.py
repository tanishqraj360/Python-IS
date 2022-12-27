fname=input('Enter file name/directory: ')
with open(fname,'r') as f:
    read=f.read()
    word=read.split()
l=[]
for i in word:
    l.append(i)

l.sort()

wname=input('Enter file name to create: ')
with open(wname,'w') as w:
    for j in l:
        w.write(j)
        w.write('\n')
