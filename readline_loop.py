f=open('file1.txt','r')
a=f.readline()
while a!="":
    print(a)
    a=f.readline()
f.close()
