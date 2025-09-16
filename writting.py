f=open('file1.txt','r')
f2=open('file2.txt','w')
a=f.readline()
while a!="":
    f2.write(a)
    a=f.readline()
f.close()
f2.close()
