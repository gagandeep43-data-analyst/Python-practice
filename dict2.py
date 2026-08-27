product={
    "name":"Laptop",
    "price":55000,
    "quantity":2
}
total=product["price"]*product["quantity"]

print("product:",product["name"])
print("price:",product["price"])
print("quantity:",product["quantity"])
print("total bill:",total)


student={
    "name":"Riya",
    "python":90,
    "math":85,
    "english":80
}

total=student["python"]+student["math"]+student["english"]
percentage=total/3

print("name:",student["name"])
print("total marks:",total)
print("percentage:",percentage)