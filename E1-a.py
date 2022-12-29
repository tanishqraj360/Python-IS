class student():
    def __init__(self, name,usn):
        self.name=name
        self.usn=usn
        self.marks=[]
        self.subject=[]
        self.calc=[]

    def sub(self):
        for i in range(3):
            subj=input('Enter subject: ')
            m=int(input('Enter marks of %s in %s: '%(self.name, subj)))
            self.marks.append(m)
            self.subject.append(subj)

    def total(self):
        total=self.marks[0]+self.marks[1]+self.marks[2]

    def per(self):
        per=(self.marks[0]+self.marks[1]+self.marks[2])/3
        

    def disp(self):
        print(self.name,'USN:',self.usn,'got',self.marks,'in',self.subject)
        print('Total marks:',self.total())
        print('Percentage:',self.per())

def estu():
    name=input('Enter name of student: ')
    usn=input('Enter USN: ')
    s1=student(name, usn)
    s1.sub()
    s1.disp()
    print('')

def main():
    print('Student Database')
    print('1. Enter Student')
    print('2. Exit')
    ch=int(input('Enter choice: '))
    if ch==1:
            estu()
            main()
    elif ch==2:
        quit()
    else:
        print('Try Again. Wrong input')
        main()

main()