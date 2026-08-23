#1 print no. from one to 10:

for i in range(1,11):
    print(i)

i = 1
while i<=10:
    print(i)
    i +=1

#2 print no. from 10 to 1:

for i in range(10,1,-1):
    print(i)

i = 10
while i >=1:
    print(i)
    i -=1

#3 Print even no. from 1 to 20:

for i in range(1,21):
    if i %2 ==0:
        print(i)

i = 1
while i <=20:
    if i %2==0:
        print(i)
    i+=1

i = 1
while i <=20:
    if i %2==0:
        print(i)
        i+=1

#4.Print odd numbers from 1 to 20:

for i in range(1,21):
    if i %2!=0:
        print("this is an odd no.",i)

i = 1
while i <=21:
    if i %2!=0:
        print(i)
    i +=1

#5.Print the multiple table of 5:

for i in range(1,11,1):
    print(5*i)

i = 1
while i <=10:
    print(5*i)
    i +=1

#6.Print the multiplication table of any no. entered by the user:

a = int(input("enter your no.:"))
for i in range(1,11,1):
    print(a*i)

a = int(input("enter your no.: "))
i = 1
while i<=10:
    print(a*i)
    i +=1
#7.Find the sum of no. from 1 to 10:
a = 0
for i in range(1,11):
    a = a+i
print(a)

a = 0
i = 1
while i <=10:
    a = a+i
    i+=1
print(a)

#8.Find the sum of first n no.:

a = 0
b = int(input("enter your no.: "))
for i in range(b+1):
    a = a+i
print(a)

a = 0
i = 1
b = int(input("enter your no.: "))
while i<=b:
    a = a+i
    i+=1
print(a)    
  #9.Find the factorial of a number:
a = int(input("enter your no.: "))
i = 1
b =1
while i <=a:
    b=b*i
    i+=1
print(b)    

#10.Reverse a number:
n = int(input('enter your number: '))
while n >0:
    r = n%10
    print(r,end="")
    n = n//10

#11.Count the digits in a given number:

n= "7857"
i = 1
while i<=len(n):
    i+=1
print(i)    

num = 123456
i = 0
while num!=0:
    num = num//10
    i +=1
print(i)    

#12.Find the sum of digits.

a = int(input("enter your number: "))
sum = 0
while a>0:
    i = a%10
    a = a//10
    sum = sum +i
print(sum)

#13.Check if a number is positive negative or zero using loop.

while True:
    
    a = int(input("enter your number: "))
    if a>0:
        print("Positive",a)
    elif a<0:
        print("Negative",a)
    else:
        print("zero",a)
    choise = input("are you want to check for another number(Yes/No): ")
    if choise.lower()=="no":
        print("program ended")
        break
#14.Check whether a number is prime.

num = int(input("enter a number: "))
for i in range(2,num):
    if num%i==0:
        print("number is not prime")
        break
else:
    print("number is a prime number")

num = int(input("enter a number: "))
i = 2
while i<num:
    if num%i==0:
        print("number is not prime")
        break
    else:
        print("number is prime")
        break

#15.Print all prime numbers from 1 to 100.

for num in range(2,101):
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)  

#16.Find the largest number from the user input.


while True:
    num1 = int(input("enter first number:"))
    num2 = int(input("enter second number:"))
    if num1>num2:
        print(num1)
    else:
        print(num2)
    Again= input("are you want to check for another no:(yes/no)")
    if Again.lower()=="no":
        print("ended")
        break

n = int(input("enter numbers in which you want to check:"))
largest = None
i = 1
while i <=n:
    num = int(input("enter a number: "))
    if largest is None or num>largest:
        largest=num
    i +=1
print(largest)   

#17.Find the smallest number from the user input.

n = int(input("enter number in which you want to check:"))
smallest = None
i = 1
while i <=n:
    num=int(input("enter a number:"))
    if smallest is None or num<smallest:
        smallest=num
    i+=1
print(smallest) 

#18. Find the factroial of a number.

a = int(input("enter your number: "))
i = 1
b = 1
while i<=a:
        b = b*i
        i+=1
print(b)
        
#19.Reverse a number.

a = input("enter your number: ")
i = 0
while True:
    print(a[::-1])
    break

a = int(input("enter your number: "))
while a>0:
    i = a%10
    print(i,end="")
    a = a//10

#20.Count the digits in a number.

a = input("enter your number: ")
i = 0
while i<=len(a)-1:
    print(len(a))
    break

a = int(input("enter your number: "))
i = 0
while a!=0:
    a = a//10
    i +=1
print(i)

#21.Find the sum of digits.

a = int(input("enter your number: "))
sum = 0
while a>0:
    i = a%10
    a = a//10
    sum = sum +i
print(sum)

#22.Check if a number is positive negative or zero using loop.

while True:
    
    a = int(input("enter your number: "))
    if a>0:
        print("Positive",a)
    elif a<0:
        print("Negative",a)
    else:
        print("zero",a)
    choise = input("are you want to check for another number(Yes/No): ")
    if choise.lower()=="no":
        print("program ended")
        break

##23.Guess the secret number using a while loop.
while True:
    a = int(input("Guess a number:"))
    if a==114801:
        print("correct number!")
        break
    else:
        print("incorrect")

secret_num = 11
a = int(input("Guess the number:"))
while a!=secret_num:
    print("incorrect")
    a = int(input("Try again!"))

print("correct!!")  

##24.Password checking program with limited attempts.

password = "Gagan123"
attempt = 1
while attempt<3:
        guess = input("enter your password: ")
        if guess!=password:
            print("Incorrect Try again:")
            attempt+=1   
        elif guess==password:
            print("correct")
            break

##25.Keep taking input until the user enters "stop".

text = input("enter something(write stop for exit): ")
while text!="stop":
    print("your entered text:",text)
    text = input("enter something(write stop for exit): ")
print("program ended")    

##26.Find the average of N numbers.

count = 1
sum = 0
num1 = int(input("enter the number:"))
while count<=num1:
    num = int(input("enter a number:"))
    sum = sum+num
    count+=1
average = sum/num1
print(average)    

#27.Print all factors of a number.

num = int(input("enter a number:"))
count = 1
print("factors are:")
while count<=num:
    if num%count == 0:
        print(count)
    count+=1
#28.Print a square star pattern.

n = 5
i = 1
while i <=n:
    print("*"*n)
    i +=1
n= 5
for i in range(n):
    print("*"*n)

#29.Right Triangle

n= int(input("enter a number:"))
i = 1
while i<=n:
    print("*"*i)
    i+=1

##30.Inverted triangle.

n = int(input("enter a number:"))
i = 0
while i<=n:
    print("*"*(n-i))
    i+=1

##31.Number pattern.

for i in range(6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

i = 1
while i<=5:
    j = 1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()    
    i+=1    

i = 1
while i<=10:
    print(i)
    i+=1

##32.
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
for i in range(1,6):
    for j in range(i):
        print(j+1,end=" ")
    print()
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()    

##33.
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()  

##34.
'''
12345
1234
123
12
1
'''  
for i in range(5,0,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()    
'''
54321
5432
543
54
5
'''
for i in range(6):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()    

##35.
'''
A
A B
A B C
A B C D
A B C D E
'''
for i in range(6):
    a="ABCDE"
    for j in range(i):
        print(a[j],end=" ")
    print()   

##36.print multiplication table from 1 to 10.

for i in range(1,11):
        for j in range(1,11):
                print(i*j)
        print()     

##37.Nested loop with rows and columns.

rows = 4
column = 5
for i in range(rows):
    for j in range(column):
        print("*",end=" ")
    print()

##38.print rectangle using star.

rows = 4
column = 8
for i in range(rows):
    for j in range(column):
        print("*",end=" ")
    print()
  
# Star pattern
n = int(input("enter a number: "))
i = 1
while i <=n:
    print(" "*(n-i),end="")
    print(("*")*(2*i-1),end="")
    print("\n")
    i +=1

n = int(input("enter a number: "))
i = 1
while i <=n:
    print("*"*i,end="")
    print("\n")
    i +=1

n = int(input("enter a number: "))
i = 1
while i <=n:
    if i==i and i==n:
        print(("*")*n,end = "")
    else:
        print(("*"),end="")
        print((" ")*(n-2),end="")
        print("*",end="")
        print("\n")   
        break
  for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    

for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print() 

for i in range(6):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()

for i in range(6):
    a = "ABCDE"
    for j in range(i):
        print(a[j],end=" ")
    print()

for i in range(1,11):
        for j in range(1,11):
                print(i*j)
        print()    
   



    
        

    



        
  






    
        
    
    
