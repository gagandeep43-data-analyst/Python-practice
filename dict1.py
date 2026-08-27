student={
"name":"Aman",
"Age":20,
"course":"Data scinece",
"marks":85
}

print("original Dictionary:")
print(student)

# #access Value
print(student["name"])
print(student["course"])

# #update value
student["marks"]=90
print(student)

#Add new key
student["city"]="kalanwali"
print(student)

# #Dictionary Method
print("keys:",student.keys())
print("values:",student.values())
print("items:",student.items())

#update mathod
student.update({"phone":"9817158409"})
print(student)

# #membership
print("name"in student)
print("salary"not in student)

#copy dictionary
new_student=student.copy()
print(new_student)

# #remove item using pop()
student.pop("city")
print("after pop:")
print(student)

# #Remove last item using pop()
student.popitem()
print(student)

# #Delete Dictionary
del student["Age"]
print(student)



#Clear copy
new_student=student.copy()
new_student.clear()
print(new_student)
