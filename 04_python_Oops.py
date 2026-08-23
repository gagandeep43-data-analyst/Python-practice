##class and objects
class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)

m1 = Mobile("Samsung", 20000)
m1.display()

m2 = Mobile("iphn",200000000)
m2.display()

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

b1 = Book("Python Basics", "John")
b1.display()

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def result(self):
        if self.marks >= 40:
            print(self.name, "Passed")
        else:
            print(self.name, "Failed")


s1 = Student("Gagan", 75)
s2 = Student("Aman", 30)

s1.result()
s2.result()

class Calculator:

    def add(self, a, b):
        print("Addition:", a + b)

    def subtract(self, a, b):
        print("Subtraction:", a - b)


c = Calculator()

c.add(10, 5)
c.subtract(10, 5)

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        self.salary = self.salary + (self.salary * 10 / 100)
        print("Name:", self.name)
        print("New Salary:", self.salary)


e1 = Employee("Gagan", 20000)

e1.increase_salary()


