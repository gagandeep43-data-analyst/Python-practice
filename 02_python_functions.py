#1.Fuction with no parameter.

def greet():
    print("hello")
greet()
greet()    

#2.Fuction with one parameter.

def greet(name):
    print("hello",name)
greet("gagan")    
greet("raman")

#3.Function with multiple parameter.

def greet(a,b):
    print("sum", a+b)
greet(2,5)    
greet(6,90)

#4.Fuction returning a value.

def greet(a,b):
    return a*b
a = greet(2,7)
print(a)

def square(num):
    return num*num
result= square(10)
print(result)

def square(num):
    return num*num
print(square(9))

#5.Even or odd number.

def number(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(number(4))    
print(number(7))    
print(number(17865))    
print(number(48628))    
print(number(24297))   

def number(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
number(6)
number(6985)
number(854738)
number(858489)
 
#6.Find maximum.

def number(a,b):
    if a>b:
        return a
    else:
        return b
print(number(56,98))
print(number(6949,98))
print(number(56,98996))

#7.Factorial using function.

def factorial(num):
    b = 1
    for i in range(1,num+1):
        b = b*i
    return b
print(factorial(4))    
print(factorial(5))    

num = 5
b = 1
for i in range(1,num+1):
    b = b*i
print(b)

#8.Print prime numbers using function.

def primenum(num):
        if num<=1:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        else:
            return True        
print(primenum(13))
print(primenum(17))
print(primenum(12))
print(primenum(23))

#9.Sum of list

def list(numbers):
    total = 0
    for i in numbers:
        total=total+i
    return total
print(list([12,5,6]))
print(list([3,6,9]))

#10.Count vowels.

def countvl(text):
    count = 0
    for chr in text.lower():
        if chr in "aeiou":
            count+=1
    return count
print(countvl("python"))    
print(countvl("programming"))  

#11.Default parameter.

def greet(name="student"):
    print("hello",name)  
greet("gagan")    
greet()

#12.Keyword arguments.

def student(name,age):
    print(name,age)
student(age=23,name="gagan")    

#13.Variable length arguments.(*arg)

def total(*numbers):
    print(numbers)
total(10,20)    
total(10,20,30,40)
total(10,20,30,40,50,60)


#14.lambda function.

square= lambda x: x*x
print(square(6))

sum = lambda a,b: a+b
print(sum(12,7))



















