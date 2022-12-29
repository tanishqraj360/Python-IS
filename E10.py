class Student():
    def __init__(self, name, usn):
        self.name=name
        self.usn=usn
        self.marks=[]
        self.subjects=[]
        

    def enterMarks(self):
        for i in range(3):
            sub=input('Enter subject: ')
            self.subjects.append(sub)
            mark=int(input('Enter marks of %s in %s: '%(self.name,sub)))
            self.marks.append(mark)
    
    def total(self):
            total=self.marks[0]+self.marks[1]+self.marks[2]
            return total
            

    def per(self):
        per=(self.marks[0]+self.marks[1]+self.marks[2])/3
        return per  
        
    def disp(self):
        print(self.name,'USN:',self.usn,'got',self.marks,'in',self.subjects)
        print('Total marks:',self.total())
        print('Percentage:',self.per())


name=input('Enter name of student: ')
usn=input('Enter USN: ')
s1=Student(name,usn)
s1.enterMarks()
s1.disp()
