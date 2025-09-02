d={'eno':123,"ename":"abc"}
print(d)
print(d['eno'])
print(d.get("ename"))
d["ename"]='xyz'
print(d)
d['age']=19
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,":",value)

d.pop("eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)
