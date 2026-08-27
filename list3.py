
child={
    "child1":{
    "name":"Raman",
    "age":8,
    "marks":400
},
"child2":
{
    "name1":"Riya",
    "age":33,
    "marks":657
}
}
print(child)
child["age"]=34
print(child)

child["city"]="Delhi"
print(child)

child.pop("age")
print(child)

child.popitem()
print(child)

child.clear()
print(child)

print(len(child))
print(child.keys())
print(child.values())
print(child.items())

new_child=child.copy()
print(child)

print("name"in child)
print("age"not in child)

