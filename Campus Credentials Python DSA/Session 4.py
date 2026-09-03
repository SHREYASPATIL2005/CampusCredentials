"""
# Dictionary in Python

# A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.
# {}
# dict()
# collection of key-value pairs ( different data types)
# key : immutable / unique
# value : mutable / can be duplicate

from numpy import iterable


d = {}
print(type(d))  # Output: <class 'dict'>
print(d)        # Output: {}

# Creating a dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"

# Accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30
print(my_dict["city"])  # Output: New York
print(my_dict["email"]) # Output: alice@example.com

# Updating a value in a dictionary
my_dict["age"] = 31
print(my_dict["age"])  # Output: 31

# Removing a key-value pair
del my_dict["city"]

# Checking if a key exists in the dictionary
if "city" in my_dict:
    print("City exists in the dictionary.")
else:
    print("City does not exist in the dictionary.")  # Output: City does not exist in the dictionary.

student={
    "roll": 12,
    "name": "John",
    "marks": 85,
    "age": 20
}
for key in student:
    print(key) # Output: roll name marks age

for value in student.values():
    print(value) # Output: 12 John 85 20

for i in student:
    print(i, ":", student[i]) # Output: [ i : student[i]] [key : value] pairs in the dictionary

for key, value in student.items():
    print(key, ":", value) # Output: [key : value] pairs in the dictionary

a = 10,20
print(type(a)) # Output: <class 'tuple'>
print(a)       # Output: (10, 20)

a,b = 10,20
print(a) # Output: 10
print(b) # Output: 20
print(a,b) # Output: 10 20

for i,j in student.items():
    print(i, ":", j) # Output: [key : value] pairs in the dictionary

student['student']={
    "roll": 12,
    "name": "Shreyas",
    "marks": 85,
    "age": 20
}

print(student) # Output: {'roll': 12, 'name': 'John', 'marks': 85, 'age': 20, 'student': {'roll': 12, 'name': 'John', 'marks': 85, 'age': 20}}

x = {"Student":["m1","m2","m3"],"roll":45}
student.update(x)
print(student)

detais = {
    "name": "Shreyas",
    "age": 20,
    #"gender": "Male",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    },
    "city": "New York",
    "email": "shreyas@example.com"
}

print(detais["address"]["city"]) # Output: New York
# print(detais["gender"]) # Output: KeyError: 'gender' (since the key "gender" does not exist in the dictionary)
# print(detais.get("gender")) # Output: None
print(detais.get("gender", "Not specified")) # Output: Not specified
# print(details[gender, "Not specified"]) # Output: Not specified # SyntaxError: invalid syntax , Use .get() method to avoid KeyError when accessing a key that may not exist in the dictionary.

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
d = {i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(d) # Output: {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}


# higher order function: A higher-order function is a function that takes one or more functions as arguments and/or returns a function as its result. In Python, functions are first-class objects, which means they can be passed around and used as arguments just like any other object (string, int, float, list, and so on).
# passing function as an argument to another function

# map, filter, reduce, sorted, min, max, sum, any, all, zip, enumerate, map(), filter(), reduce(), sorted(), min(), max(), sum(), any(), all(), zip(), enumerate() are some of the higher order functions in Python.

# 1. map():
# auto increment of a number by 1
# take function as a parameter
# iterable object : generate  iterable solutions (list, tuple, set, dictionary, string)
# map(function, iterable) # function is applied to each element of the iterable and returns a new iterable with the results.
def sqr(no):
    return no**2

l = [1,2,3,4,5]
result = list(map(sqr, l))
print(result) # Output: [1, 4, 9, 16, 25]

# lambda with map()
result = list(map(lambda no:no**2, l))
print(result) # Output: [1, 4, 9, 16, 25]

l = [1,2,3,4,5]
print(list(map(lambda no:no**2, l))) # Output: [1, 4, 9, 16, 25]

l = [1,2,3,4,5]
# use int in this
# print(list(map(int, lambda no:no**2, l))) # Output: [1, 4, 9, 16, 25]

a,b,c = map(int, input("Enter three numbers: ").split())
print("a:", a)
print("b:", b)
print("c:", c)

# [1,2,3]
a = list(map(int, input("Enter three numbers: ").split()))
print(a) # Output: [1, 2, 3]

# coma separated values # 12,3,4
a,b,c = map(int, input("Enter three numbers: ").split(','))
print(a, b, c) # Output: 12 3 4

l1 = [1,2,3]
l2 = [4,5,6]
op = [ 11, 22, 33]

def fun(x,y):
    return x+y
print(list(map(fun, l1, l2))) # Output: [5, 7, 9]

# 2. filter()
# filter() function is used to filter the elements of an iterable based on a given condition. It takes a function and an iterable as arguments and returns a new iterable containing only the elements that satisfy the condition defined in the function.
# 
l = [1,2,3,4,5,6,7,8,9,10]
def is_even(no):
    return no%2==0

data = list(filter(is_even, l))
print(data) # Output: [2, 4, 6, 8, 10]

print(list(filter(lambda no:no%2==0, l))) # Output: [2, 4, 6, 8, 10]
"""

# Doubt ?
l = ['  5  '," raj ","    87  "]
op = [5,87]
print(list(filter(lambda x: x.strip().isdigit(), l))) # Output: ['  5  ', '    87  ']

l = ['  5  '," raj ","    87  "]
# using map and filter combined for this
print(list(map(lambda x: int(x.strip()), filter(lambda x: x.strip().isdigit(), l)))) # Output: [5, 87] 
# Explain this code: 
# The filter function is used to filter out the elements that are not digits after stripping whitespace. The map function is then used to convert the remaining elements to integers.

# enumerate(): The enumerate() function in Python is used to add a counter to an iterable (e.g., list, tuple, string) and returns it as an enumerate object. This is useful when you want to iterate over an iterable and keep track of the index of each element.
# index and value
# The enumerate() function takes an iterable as an argument and returns an enumerate object, which can be converted into a list or tuple using the list() or tuple() functions.


l = [1,2,3,4,5]
for i in l:
    print(i) # Output: 1 2 3 4 5

for i in range(len(l)):
    print(i) # Output: 0 1 2 3 4

for i in range(len(l)):
    print(i, l[i]) # Output: 0 1 1 2 2 3 3 4 4

l = ["apple", "banana", "cherry", "date", "mango", "kiwi", "grape", "orange", "pear", "peach", "bulbery", "watermelon", "pineapple", "strawberry", "blueberry", "raspberry", "blackberry", "cantaloupe", "honeydew", "papaya"]
for i, v in enumerate(l):
    print(i, v) # Output: 0 apple 1 banana 2 cherry 3 date 4 mango 5 kiwi 6 grape 7 orange 8 pear 9 peach 10 bulbery 11 watermelon 12 pineapple 13 strawberry 14 blueberry 15 raspberries 16 blackberries 17 cantaloupe 18 honeydew 19 papaya

for i, v in enumerate(l, start=1):
    print(i, v) # Output: 1 apple 2 banana 3 cherry 4 date 5 mango 6 kiwi 7 grape 8 orange 9 pear 10 peach 11 bulbery 12 watermelon 13 pineapple 14 strawberry 15 blueberry 16 raspberries 17 blackberries 18 cantaloupe 19 honeydew 20 papaya

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i, j in enumerate(l):
    if j%2 == 0:
        print(i, j) # Output: 0 10 1 20 2 30 3 40 4 50 5 60 6 70 7 80 8 90 9 100


l = [5, 6, 7, 8, 9, 10]
print(list(enumerate(l))) # Output: [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

for i, j in enumerate(l):
    if j == 8:
        print(i, j) # Output: 3 8

s="Hello, World!"
for i, j in enumerate(s):
    if j in "aeiouAEIOU":
        print(i, j) # Output: 1 e 4 o 7 o

l = [1,2,3,4,5]
for i, j in enumerate(reversed(l)):
    print(i, j) # Output: 0 5 1 4 2 3 3 2 4 1

# two sum
print("Two Sum Problem")
l = [1, 2, 4, 7, 11, 15]
target = 9
d = {}
# op = [1,3] [2,5]
for i,j in enumerate(l):
    ans = target - j
    if ans in d:
        print([d[ans], i]) # Output: [1, 3]
        # break
    d[j] = i

# Dry run of the above code:
# i=0, j=1, ans=8, d={} -> d[1]=0
# i=1, j=2, ans=7, d={1: 0} -> d[2]=1
# i=2, j=4, ans=5, d={1: 0, 2: 1} -> d[4]=2
# i=3, j=7, ans=2, d={1: 0, 2: 1, 4: 2} -> 2 in d -> print([d[2], 3]) -> [1, 3]

# reduce(): The reduce() function in Python is used to apply a specified function cumulatively to the items of an iterable, reducing the iterable to a single value. It is part of the functools module, so you need to import it before using it.
# The reduce() function takes two arguments: a function and an iterable. The function should take two arguments and return a single value. The reduce() function applies the function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value.
from functools import reduce
l = [1, 2, 3, 4, 5]
sum = 0
for i in l:
    sum = sum + i
print(sum) # Output: 15
print(reduce(lambda x, y: x + y, l)) # Output: 15
print(reduce(lambda x, y: x * y, l)) # Output: 120

# and or
print(reduce(lambda x, y: x and y, [True, True, False, True])) # Output: False
print(reduce(lambda x, y: x or y, [False, False, True, False])) # Output: True

# OPP : Object Oriented Programming
class Student:
    # self is used in class in functions to access the attributes and methods of the class. It refers to the instance of the class itself.
    # object is used outside the class to access class attributes and methods. It refers to the instance of the class that is created outside the class.
    def accept(self, roll,name,per):
        self.name = name
        self.percentage = per

    def display(self):
        print(self.name, self.percentage)

s1=Student()
s1.accept(12, "Shreyas", 85)
s1.display()

# Constructor: A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object. In Python, the constructor method is defined using the __init__() method.
# Constructor is nothing but special type of function 
# It is inside class ( member of a class)
# It's name is same class name
# It its automatically call when object is created
# It is used to initialize the attributes of the object.

class Student:
    def __init__(self,roll,name,per):
        self.roll = roll
        self.name = name
        self.percentage = per

    def display(self):
        print(self.roll, self.name, self.percentage)

s1=Student(12, "Shreyas", 85)
s1.display()

# Static Variable and Method:

# Static Variable : Throught the program single copy exists called by class name as well as variable name but as per rule called by class name

# Static Var: 
# 1000 object : 1 copy of static variable
# 100 object : 1 copy of static variable
# 1 object : 1 copy of static variable
# No object : 1 copy of static variable 


"""
class Student:
    def __init__(self,roll,name,clg):
        self.roll = roll
        self.name = name
        self.clg = clg

    def display(self):
        print(self.roll, self.name, self.clg)

s1=Student(12, "Shreyas", "MIT")
s1.display()

s2=Student(13, "Rohit", "MIT")
s2.display()

s3=Student(14, "Priya", "MIT")
s3.display() """

class Student:
    clg = "MIT"  # Static variable
    def __init__(self,roll,name):
        self.roll = roll
        self.name = name

    def display(self):
        print(self.roll, self.name, self.clg)
        print("College Name:", Student.clg)  # Accessing static variable using class name

s1=Student(12, "Shreyas")
s1.display()

s2=Student(13, "Rohit")
s2.display()

s3=Student(14, "Priya")
s3.display()

print("College Name:", Student.clg)  # Accessing static variable using class name
print("College Name:", s1.clg)  # Accessing static variable using object name
print("College Name:", s2.clg)  # Accessing static variable using object name
print("College Name:", s3.clg)  # Accessing static variable using object name
print(s1.roll, s1.name, s1.clg)


# Pillars of Object Oriented Programming (OOP):
# 1. Encapsulation: Encapsulation is the process of bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class. It restricts direct access to some of the object's components, which can prevent the accidental modification of data. In Python, encapsulation is achieved using private and protected access modifiers.
# 2. Inheritance: Inheritance is a mechanism in OOP that allows a class (called a child or subclass) to inherit attributes and methods from another class (called a parent or superclass). This promotes code reusability and establishes a hierarchical relationship between classes. In Python, inheritance is implemented by passing the parent class as an argument to the child class.
      # single
      # multiple
      # multilevel
      # hierarchical
      # hybrid
# 3. Polymorphism: Polymorphism is the ability of different classes to be treated as instances of the same class through a common interface. It allows methods to do different things based on the object it is acting upon, even if they share the same name. In Python, polymorphism can be achieved through method overriding and operator overloading.
      # compile : method overloading
      # Runtime : method overriding
# 4. Abstraction: Abstraction is the concept of hiding the complex implementation details of a system and exposing only the essential features to the user. It allows users to interact with an object at a higher level without needing to understand its internal workings. In Python, abstraction can be achieved using abstract classes and interfaces, which define methods that must be implemented by subclasses.

# Access Specifiers in Python:
  # Public: Public members (attributes and methods) are accessible from anywhere, both inside and outside the class. By default, all members in Python are public unless specified otherwise.
  # Protected: Protected members are intended to be accessed only within the class and its subclasses. They are denoted by a single underscore prefix (e.g., _protected_member). However, this is just a convention, and Python does not enforce strict access control.
  # Private: Private members are intended to be accessed only within the class itself. They are denoted by a double underscore prefix (e.g., __private_member). Python uses name mangling to make it harder to access private members from outside the class, but it is still possible to do so if needed.

# Single Inheritance:
class Parent:
        def parent_method(self):
            print("This is a method in the Parent class.")

class Child(Parent):
        def child_method(self):
            print("This is a method in the Child class.")
            self.parent_method()  # Calling the parent method from the child class

# Multiple Inheritance:
class Parent1:
        def parent1_method(self):
            print("This is a method in the Parent1 class.")
class Parent2:
        def parent2_method(self):
            print("This is a method in the Parent2 class.")

class Child(Parent1, Parent2):
        def child_method(self):
            print("This is a method in the Child class.")
            self.parent1_method()  # Calling the method from Parent1
            self.parent2_method()  # Calling the method from Parent2

class GrandChild(Child):
        def grandchild_method(self):
            print("This is a method in the GrandChild class.")
            self.parent1_method()
            self.parent2_method()
            self.child_method()
            self.grandchild_method()

# Multilevel Inheritance:
class Parent:
        def parent_method(self):
            print("This is a method in the Parent class.")
class Child(Parent):
        def child_method(self):
            print("This is a method in the Child class.")
            self.parent_method()  # Calling the parent method from the child class
class GrandChild(Child):
        def grandchild_method(self):
            print("This is a method in the GrandChild class.")
            self.parent_method()
            self.child_method()
            self.grandchild_method()

# Hierarchical Inheritance:
class Parent:
        def parent_method(self):
            print("This is a method in the Parent class.")
            self.parent_method()
class Child1(Parent):
        def child_method(self):
            print("This is a method in the Child class.")
        def grandchild_method(self):
            print("This is a method in the GrandChild class.")
