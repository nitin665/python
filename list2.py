a=[1,2,3,4]
b=[]
n=int(input("enter the number of elements you want "))
for i in range(0,n):
    x=int(input("enter the element"))
    b.append(x)
a.extend(b)
print(a)
