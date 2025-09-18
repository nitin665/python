class stud:
    def __init__(self,a,b,c,m1,m2,m3):
        self.sno=a
        self.sname=b
        self.sage=c
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def calculate(self):
        t=m1+m2+m3
        avg=t/3
        print("total marks ",t)
        print("average ",avg)
        if m1>=40 and m2>=40 and m3>=40:
            self.result="pass"
        else:
            self.result="fail"

    def display(self):
        print("student no:",self.sno)
        print("student name",self.sname)
        print("student age",self.sage)
        print("mark 1",m1)
        print("mark 2",m2)
        print("mark 3",m3)
        print(self.result)

x=int(input("enter roll no"))
y=input("enter name")
z=int(input("enter age"))
m1=int(input("enter m1"))
m2=int(input("enter m2"))
m3=int(input("enter m3"))
obj=stud(x,y,z,m1,m2,m3)
obj.calculate()
obj.display()
