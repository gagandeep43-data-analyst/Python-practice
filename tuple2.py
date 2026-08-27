student=("Aman",20,"Data Science",85,85)
print("OriginalTuple:",student)

#indexing
print("name:",student[0])
print("Course:",student[2])

#Negative indexing
print("Last Value:",student[-1])

#slicing
print("First 3 Values:",student[:3])
print("Last 2 Values:",student[-2:])

#Functions
print("Length:",len(student))
print("Maximum Marks:",max(student[-2:]))
print("Minimum Marks:",min(student[-2:]))

# methods
print("Count of 85:",student.count(85))
print("index of Data Science:",student.index("Data Science"))

#Membership
print("Aman"in student)
print("Python"not in student)

#Concatenation
extra=("Delhi","India")
print("After Concatention:",student+extra)

#Repetition
print(("Python",)*3)

# Nested Tuple
marks=((80,90),(70,85))
print("Nested Tuple:",marks)
print("First Student Marks:",marks[0])
print("Second Subject Marks:",marks[1][1])

# Packing
teacher="Rahul",30,"Python"
print("Packed Tuple:",teacher)

# Unpaking
name,age,course,mark1,mark2=student
print(name)
print(age)
print(course)

#Tuple to list
student_list=list(student)
print(student_list)

#List to Tuple
new_tuple=tuple(student_list)
print(new_tuple)