from datetime import datetime
name=input('Enter name of person: ')
yob=int(input('Enter Year of Birth of %s'%(name)))
age=datetime.now().year-yob
if age>=60:
    print('%s is a senior citizen.'%(name))
else:
    print('%s is not a senior citizen.'%(name))
    