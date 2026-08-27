name=["rama","roop","veena","beant","veena"]
name.sort()
print(name)
print(name.count("veena"))
name[2]="Moto"
print(name)

name.append("Sanjna")
print(name)

name.insert(3,"Reenu")
print(name)
name.extend(["Gogi","Nargis","Manoj"])
print(name)

name.remove("Reenu")
print(name)

name.pop(2)
print(name)

del name[0]
print(name)

name.clear()
print(name)

print(len(name))
print(max(name[-4:]))
print(min(name[-4:]))
print(sum(name[-4:]))

name.sort()
print(name)

name.reverse()
print(name)

print(name.count("rama"))

print(name.index("rama"))

b=name.copy()
print(b)

print("rama"in name)
name=["rama"]

a=["moto","veena","roop"]
b=[23,45,67]
c=(a+b)
print(c)

a=[[23,56,67],[54,78,56]]
print(a)
print(a[0])
print(a[0][1])

name1=input("enter your first name:")
name2=input("enter your second name:")
name3=input("enter your third name")
students=[name1,name2,name3]
print(students)