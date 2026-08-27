items=["Milk","Bread","Egg","Rice","Milk"]
print(items)

#Indexing
print(items[2])
print(items[-2])

#slicing
print(items[2:])
print(items[-3:])

#Update
items[1]="Butter"
print(items)

#Add Element
items.append("Suger")
print(items)

items.insert(0,"Tea")
print(items)

items.extend(["soap","oil"])
print(items)

#Remove Elements
items.remove("Milk")
print(items)

items.pop()
print(items)

del items[3]
print(items)

#functions
print(len(items))
print(items.count("Milk"))
print(items.index("Rice"))

#copy
new_items=items.copy()
print(new_items)

# Membership
print("Tea" in items)
print("Coffee" not in items)

# Repetition
print(["Buy"]*4)

#Nested List
price=[[50,30],[70,90]]
print(price)
print(price[0][1])
print(price[1][0])

#concatenation
more=["salt","juice"]
print(items+more)

#clear
new_items.clear()
print(new_items)

