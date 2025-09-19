class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("student no: ",self.sno)
        print("student name ",self.sname)
        print("student age ",self.sage)

class marks(stud):
    def __init__(self,a,b,c,m1,m2,m3):
        super().__init__(a,b,c)
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def display(self):
        super().display() 
        print("mark 1 ",self.mark1)
        print("mark 2 ",self.mark2)
        print("mark 3 ",self.mark3)

x=int(input("enter roll no "))
y=input("enter name ")
z=int(input("enter age "))
m1=int(input("enter m1 "))
m2=int(input("enter m2 "))
m3=int(input("enter m3 "))
obj=marks(x,y,z,m1,m2,m3)
obj.display()
