laptop=("dell","black","528",50000,50000)
print("original tuple:",laptop)

#indexing
print("brand:",laptop[0])
print("color:",laptop[1])

#functions
print("length:",len(laptop))
print("higest price:",max(laptop[-2:]))
print("lowest price:",min(laptop[-2:]))

# methods
print("count of 50000:",laptop.count(50000))
print("index of black:",laptop.index("black"))

# negative indexing
print("price:",laptop[-1])

# slicing
print(laptop[:2])
print(laptop[-2:])

# membership
print("dell" in laptop)
print("apple" not in laptop)

# concatention
offer=("1 year warranty",)
print(laptop+offer)

# repetition
print(("rama",)*1000)

#nested tuple
shop=(("dell",50000),("iphone",80000))
print(shop)
print(shop[1])
print(shop[1][0])

#packing
mobile="HP",16,"silver"
print(mobile)

#unpacking
brand,storage,color,price1,price2=laptop
print(brand)
print(storage)
print(color)

# #tuple to list
b=list(laptop)
print(b)

#list to tuple
c_tuple=tuple(b)
print(c_tuple)

