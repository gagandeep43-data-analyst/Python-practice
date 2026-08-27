mobile=("samsung",256,"Block",45000,45000)
print("original tuple:",mobile)
#indexing
print("Brand:",mobile[0])
print("color:",mobile[2])
#Negative indexing
print("price,mobile[-1]")
#slicing
print("First 2 Values:",mobile[:2])
print("Last 3 Values:",mobile[-3:])
#Functions
print("Length:",len(mobile))
print("Highest price:",max(mobile[-2:]))
print("Lowest price:",min(mobile[-2:]))
#Methods
print("count of 45000:",mobile.count(45000))
print("index of black:",mobile.index("black"))
#Membership
print("samsung" in mobile)
print("Apple"not in mobile)
#concatenation
offer=("1 year warranty",)
print(mobile+offer)
#Repetition
print(("sale",)*4)
#Nested tuple 
shop=(("samsung",45000),("phone",80000))
print(shop)
print(shop[1])
print(shop[1][0])
#packing
laptop="HP",16,"silver"
print(laptop)
#Unpacking
brand,storage,color,price1,price2=mobile
print(brand)
print(storage)
print(color)
#tuple to List
mobile_list=list(mobile)
print(mobile_list)
#List to tuple
again_tuple=tuple(mobile_list)
print(again_tuple)
