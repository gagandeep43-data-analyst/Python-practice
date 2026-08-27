name=input("enter your name:")
age=int(input("inter your age:"))
salary=int(input("inter your monthly salary:"))
cibil=int(input("enter your cibil score:)"))

print()
print("Loan Report")
print("name:",name)

if age<18:
    print("Loan Rejected")
    print("Reason: Age is below 18")

elif salary<20000:
    print("loan Rejected")
    print("Reason: Low Cibil Score")

elif cibil<650:
    print("loan rejected")
    print("Reason:low cibil score")

elif salary>=100000 and cibil>=800:
    print("Loan Approved")
    print("Loan amount:2000000")
    print("Interst rate:8%")

elif salary>=50000 and cibil>=750:
    print("loan approved")
    print("LOan Amount:1000000")
    print("interst rate: 10%")

else:
    print("Loan Approved")
    print("Loan amount:500000")
    print("interest rate:12%")
