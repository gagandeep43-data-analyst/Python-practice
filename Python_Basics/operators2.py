name="Ankit"
course="phthon"
age=21
fee=1500.50
discount=200
is_stuent=False

print("Name:",name)
print("course:",course)
print("Age:",age)
print("Original Fee:",fee)

print("Fee after Discount",fee-discount)
print("Age after 1 years:",age*2)
print("Fee*2:",fee*2)
print("Half Fee:",fee/2)

print("Age>18:",age<18)
print("Fee==1500.00",fee==1500.50)
print("Age !=25:",age!=25)

print("Eligible:",age > 18 and is_stuent)
print("special Offer:",age<18 or is_stuent)
age+=2
fee-=100

print("Updated Age:",age)
print("Updated Fee:",fee)