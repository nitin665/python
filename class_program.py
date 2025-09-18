class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("student no:",self.sno)
        print("student name",self.sname)
        print("student age",self.sage)

x=int(input("enter roll no"))
y=input("enter name")
z=int(input("enter age"))
obj=stud(x,y,z)
obj.display()
