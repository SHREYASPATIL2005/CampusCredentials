""" 
def fun(*,a,b,c):
    print(a)
    print(b)
    print(c)

fun(a=1, b=2, c=3)
fun(b=2, c=3, a=1)
fun(1, 2, 3) # Error: fun() takes 0 positional arguments but 3 were given
# Error: fun() takes 0 positional arguments but 3 were given Example: fun(1, 2, 3) # Error

def fun(*args):
    print(args)

print(fun(1, 2, 3)) # (1, 2, 3)
print(fun(a=1, b=2, c=3)) # Error: fun() got an unexpected keyword argument 'a'

def fun(**kwargs):
    print(kwargs)

print(fun(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}

def fun(**a):
    print(a)

print(fun(a=1, b=2, c=3)) # {'a': 1, 'b': 2, 'c': 3}

# 8. keyword-only parameters: Parameters that can only be specified by keyword and not positionally. They are defined using a * in the function signature.
def fun(a, b, *, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

    print(fun(1, 2, c=3, d=4)) # 1 2 3 4
    print(fun(1, 2, 3, 4)) # Error: fun() takes 2 positional arguments but 4 were given

# 9. positional-only parameters: Parameters that can only be specified positionally and not by keyword. They are defined using a / in the function signature.

def fun(a, b, /, c, d):
    print(a)
    print(b)
    print(c)
    print(d)

print(fun(1, 2, c=3, d=4)) # 1 2 3 4
print(fun(1, 2, 3, 4)) # 1 2 3 4
print(fun(a=1, b=2, c=3, d=4)) # Error: fun() got some positional-only arguments passed as keyword arguments: 'a, b'


# 10. Combining positional-only and keyword-only parameters: You can combine positional-only and keyword-only parameters in a function signature by using both / and *.
def fun(a, b, /, c, d, *, e, f):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

    print(fun(1, 2, c=3, d=4, e=5, f=6)) # 1 2 3 4 5 6
    print(fun(1, 2, 3, 4, e=5, f=6)) # 1 2 3 4 5 6
    print(fun(1, 2, 3, 4, 5, 6)) # Error: fun() takes 4 positional arguments but 6 were given

# 11 .pass statement: The pass statement is used as a placeholder for future code. It does nothing when executed. It is often used in function definitions, class definitions, and control flow statements where code will be added later.
def fun():
    pass

def food(l):
    print(l)
    print(l[0])


l = ["Pizza", "Burger", "Pasta"]
food(l)


def food(d):
    print(d)
    print(d[2])



d = {1:"Pizza", 2:"Burger", 3:"Pasta"}
food(d)

# Function replacement: You can replace a function with another function by assigning the new function to the same name as the old function. This allows you to change the behavior of the function without changing its name.
def add(x, y):
    return x + y

def add(x,y,z):
    return x + y + z

#print(add(1, 2)) # Error: add() missing 1 required positional argument: 'z'
print(add(1, 2, 3)) # 6


# Global and local variables: A global variable is a variable that is defined outside of any function and can be accessed from anywhere in the code. A local variable is a variable that is defined inside a function and can only be accessed from within that function.
x = 10 # global variable
def fun():
    x = 5 # local variable
    print(x)
    
print(x) # 10
x = 15 # global variable
fun() # 5


laptop = "HP" # global variable

def funNinja():
    laptop = "Dell" # local variable
    print(laptop)

def funNinja2():
    global laptop # global variable
    laptop = "Apple" # global variable
    print(laptop)

funNinja() # Dell
funNinja2() # Apple
print(laptop) # Apple


def funNihal():
    laptop = "Lenovo" # local variable
    print(laptop)
    shivam(laptop) # Lenovo


def shivam(laptop):

    print("from nihal:", laptop) # Lenovo

def hassan():
    pass

def funNihal():
    laptop = "Lenovo" # local variable
    return laptop


def shivam(laptop):
    funNihal() # Lenovo
    print("from nihal:", laptop) # Lenovo

def hassan():
    pass

#Helper function: A helper function is a function that is used to perform a specific task that is needed by another function. It is often used to break down a complex problem into smaller, more manageable parts.

"""
"""
# LIST in Python
# Collections of items in a particular order. It is a mutable data structure that allows you to store and manipulate a collection of elements. Lists are defined using square brackets [] and can contain elements of different data types, including other lists.
# Different data types that can be stored in a list include integers, floats, strings, booleans, and other lists. Lists can also contain elements of different data types, allowing for heterogeneous collections of data.
# Lists can be created using the list() constructor or by using square brackets [] to define a list literal. For example, you can create a list of integers using the list() constructor like this: my_list = list([1, 2, 3, 4, 5]). Alternatively, you can create a list of strings using square brackets like this: my_list = ["apple", "banana", "cherry"].
# Properties of List:
# 1. Ordered: The elements in a list are ordered, meaning that they have a specific order and can be accessed using their index.
# 2. Mutable: Lists are mutable, meaning that you can change the elements in a list after it has been created. You can add, remove, or modify elements in a list.
# 3. Allows duplicate elements: Lists can contain duplicate elements, meaning that the same value can appear multiple times in a list.
# 4. Allows heterogeneous elements: Lists can contain elements of different data types, meaning that you can have a list that contains integers, strings, and other data types all in the same list.
# 5. Dynamic: Lists are dynamic, meaning that they can grow and shrink in size as needed. You can add or remove elements from a list at any time.
# 6. Indexing and slicing: Lists support indexing and slicing, meaning that you can access individual elements or a range of elements in a list using their index.  
# 7. Iteration: Lists can be iterated over using loops, meaning that you can perform operations on each element in a list using a loop.
# 8. Nesting: Lists can be nested, meaning that you can have a list that contains other lists as elements. This allows you to create complex data structures using lists.
# 9. Built-in methods: Lists have a number of built-in methods that allow you to perform common operations on lists, such as adding or removing elements, sorting, and searching.
# 10. Memory management: Lists are implemented as dynamic arrays in Python, meaning that they are stored in contiguous blocks of memory. This allows for efficient memory management and fast access to elements in a list.
# 11. Memory overhead: Lists have a memory overhead due to the way they are implemented in Python. Each element in a list requires additional memory to store metadata, such as the size of the list and the type of each element. This can lead to increased memory usage compared to other data structures, such as arrays or linked lists.
# 12. Performance: Lists have a time complexity of O(1) for accessing elements by index, O(n) for searching for an element, and O(n) for inserting or deleting elements. This means that lists are generally efficient for small to medium-sized data sets, but may become slower for larger data sets.
# 13. Memory allocation: Lists are implemented as dynamic arrays in Python, meaning that they are allocated in contiguous blocks of memory. When a list is created, Python allocates a block of memory that is large enough to hold the initial elements of the list. If the list grows beyond this initial allocation, Python will allocate a new block of memory that is larger than the previous block and copy the elements from the old block to the new block. This process can be time-consuming and may lead to performance issues if the list grows too large.
# 14. Memory fragmentation: Lists can suffer from memory fragmentation, which occurs when the memory used by a list is not contiguous. This can happen when elements are added or removed from a list, causing gaps in the memory used by the list. Memory fragmentation can lead to increased memory usage and slower performance. 


l = [1, 2, 3, 4, 5]
print(l) # [1, 2, 3, 4, 5]

l.append(6) # [1, 2, 3, 4, 5, 6]
print(l) # [1, 2, 3, 4, 5, 6]
print(id(l)) # 140706982042752
l.append(7) # [1, 2, 3, 4, 5, 6, 7]
print(l) # [1, 2, 3, 4, 5, 6, 7]
print(id(l)) # 140706982042752

l.index(3) # 2
print(l.index(3)) # 2

# Interview Questions:
# Difference between:
# array list  arraylist linkedlist dynamicarray  dynamicarraylist  dynamicarraylistlinkedlist


l = [10,20,30]
# l=1+45 # Error: unsupported operand type(s) for +: 'list' and 'int'
l = l+[45] # [10, 20, 30, 45]
print(l) # [10, 20, 30, 45]
l1 = [1,2,3]

l = l+l1 # [10, 20, 30, 45, 1, 2, 3]
print(l) # [10, 20, 30, 45, 1, 2, 3]

l.extend([100,200,300]) # [10, 20, 30, 45, 1, 2, 3, 100, 200, 300]
print(l) # [10, 20, 30, 45, 1, 2, 3, 100, 200, 300]
l2 = [1000,2000,3000]
l.extend(l2) # [10, 20, 30, 45, 1, 2, 3, 100, 200, 300, 1000, 2000, 3000]
print(l) # [10, 20, 30, 45, 1, 2, 3, 100, 200, 300, 1000, 2000, 3000]

l = [10, 20, 30]
l1 = [200, 300, 400]
l.append(l1) # [10, 20, 30, [200, 300, 400]]
print(l) # [10, 20, 30, [200, 300, 400]]

l=[10, 20, 30]
l.pop() # [10, 20]
print(l) # [10, 20]
print(l.pop()) # 20
print(l) # [10]


l=[10, 20, 30]
l.pop(1) # [10, 30]
print(l) # [10, 30]

l=[10, 20, 30]
l.remove(20) # [10, 30]
print(l) # [10, 30]

l=[10, 20, 30]
l.remove(20) # [10, 30]
print(l) # [10, 30]

# count() method: The count() method is a built-in method in Python that is used to count the number of occurrences of a specified element in a list. It takes one argument, which is the element to be counted, and returns an integer value representing the number of times that element appears in the list.
l=[10, 20, 30, 10, 20, 30, 10]
print(l.count(10)) # 3

l = [1,2,3,4,5]
l.clear() # []
print(l) # []

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c =  a
d = b.copy() # [1, 2, 3, 4, 5]
print(a is b) # False
print(a is c) # True
print(b is d) # False
print(b is c) # False
print(c is d) # False
print(b is d) # False
print(a == b) # True
print(c == d) # True
print(a == c) # True
print(b == d) # True
print(a == d) # True
print(c == b) # True
print(a == d) # True
print(c == b) # True


# sorting a list: The sort() method is a built-in method in Python that is used to sort the elements of a list in ascending or descending order. It modifies the original list and does not return a new list. The sort() method takes an optional argument called reverse, which is a boolean value that determines whether the list should be sorted in ascending or descending order. By default, reverse is set to False, which means that the list will be sorted in ascending order. If reverse is set to True, the list will be sorted in descending order.
l = [5, 2, 9, 1, 5, 6]
l.sort() # [1, 2, 5, 5, 6, 9] # reverse=False means ascending order
print(l) # [1, 2, 5, 5, 6, 9]

l = [5, 2, 9, 1, 5, 6]
l.sort(reverse=True) # [9, 6, 5, 5, 2, 1] # reverse=True means descending order
print(l) # [9, 6, 5, 5, 2, 1]

# index() method: The index() method is a built-in method in Python that is used to find the index of the first occurrence of a specified element in a list. It takes one argument, which is the element to be searched for, and returns an integer value representing the index of the first occurrence of that element in the list. If the element is not found in the list, it raises a ValueError.
l = [1, 5, 2, 3, 5, 4, 5]
print(l.index(3)) # 2
# print(l.index(6)) # Error: ValueError: 6 is not in list
print(l.index(5, 3)) # 4
print(l.index(5, 3, 6)) # 4 # syntax: list.index(x[, start[, end]]) -> int

l = [1, 2, 34, 45, 64, 23, 12, 34, 45, 67, 89]
print(len(l)) # 11
print(max(l)) # 89
print(min(l)) # 1


l = [4,6,2,1,3,5]
l.sort() # [1, 2, 3, 4, 5, 6]
print(l[0]) # 1
print(l[len(l)-1]) # 6
print(l[len(l)-2]) # 5

"""
# minimum element in a list: The minimum element in a list is the element that is smaller than all other elements in the list. To find the minimum element in a list, you can iterate through the list and keep track of the smallest element seen so far. If you encounter an element that is smaller than the current smallest element, you update the smallest element to be the new element.
from numpy import inner


l = [4,62,2,1,3,5]
mi = l[0]
for i in range(1,len(l)):
    if l[i] < mi:
        mi = l[i]

print(mi) # 1

# maximum element in a list: The maximum element in a list is the element that is greater than all other elements in the list. To find the maximum element in a list, you can iterate through the list and keep track of the largest element seen so far. If you encounter an element that is greater than the current largest element, you update the largest element to be the new element.
l = [4,62,2,1,3,5]
ma = l[0]
for i in range(1,len(l)):
    if l[i] > ma:
        ma = l[i]
print(ma) # 62

# Second largest element in a list: The second largest element in a list is the element that is greater than all other elements except for the largest element. To find the second largest element in a list, you can iterate through the list and keep track of the largest and second largest elements seen so far. If you encounter an element that is greater than the current largest element, you update the second largest element to be the current largest element and update the largest element to be the new element. If you encounter an element that is greater than the current second largest element but less than the current largest element, you update the second largest element to be the new element.
l = [4,62,2,1,3,5]
ma = l[0]
sma = l[0]
for i in range(1,len(l)):
    if l[i] > ma :
        sma = ma
        ma = l[i]
    elif l[i] > sma and l[i] != ma:
        sma = l[i]
print(sma) # 5

l=[1,2,3,4,5]
l1=[]
for i in l:
    l1.append(i*i)
print(l1) # [1, 4, 9, 16, 25]

# lisr comprehension: List comprehension is a concise way to create lists in Python. It allows you to create a new list by applying an expression to each element of an existing iterable (such as a list, tuple, or string) and optionally filtering the elements based on a condition. The syntax for list comprehension is [expression for item in iterable if condition]. The expression is evaluated for each item in the iterable, and the resulting values are collected into a new list.
l = [1,2,3,4,5]
l1 = [i*i for i in l]
print(l1) # [1, 4, 9, 16, 25]

l = [1,2,3,4,5]
print(ans := [i*i for i in l])

print(ans := [i*i for i in [1,2,3,4,5]]) # [1, 4, 9, 16, 25]
print(ans := [i*i for i in range(1,6)]) # [1, 4, 9, 16, 25]

l=["Nashik","Pune","Mumbai","Delhi", "Nagpur"]
print(ans := [i[0] for i in l]) # ['N', 'P', 'M', 'D', 'N']

# print([i if i%2 == 0 for i in range(1,101)])
print([i for i in range(1,101) if i%2 == 0]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96


# Tuples in Python
t=(1,2,3,4,5)
print(t) # (1, 2, 3, 4, 5)
print(type(t)) # <class 'tuple'>

t=tuple()
print(t) # () # Empty tuple
print(type(t)) # <class 'tuple'>

t=(10)
print(t) # 10
print(type(t)) # <class 'int'>

t=(10,)
print(t) # (10,)
print(type(t)) # <class 'tuple'>

t=(1,2,"hello",3.14,True,None,{"key": "value"}, [1, 2, 3], (4, 5, 6))
print(t) # (1, 2, 'hello', 3.14, True, None, {'key': 'value'}, [1, 2, 3], (4, 5, 6))

t=(1,2,3,4,5)
print(t[0]) # 1
print(t[1]) # 2
print(t[0:2]) # (1, 2)

# t1=t.copy() # (1, 2, 3, 4, 5) # Error: 'tuple' object has no attribute 'copy'
# print(t1) # (1, 2, 3, 4, 5)

t = (1, 2, 3, 4, 5)
print(id(t)) # 140706982042752
t = t + (6, 7, 8)
print(t) # (1, 2, 3, 4, 5, 6, 7, 8)
print(id(t)) # 140706982042752
t = t + (9, )
print(t) # (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(id(t)) # 140706982042752

t = (34, 45, 23, 12, 34, 45, 67, 89)
print(sorted(t)) # [12, 23, 34, 34, 45, 45, 67, 89] # List
print(tuple(sorted(t))) # (12, 23, 34, 34, 45, 45, 67, 89) # Tuple
print(sorted(t, reverse=True)) # [89, 67, 45, 45, 34, 34, 23, 12] # List
print(tuple(sorted(t, reverse=True))) # (89, 67, 45, 45, 34, 34, 23, 12) # Tuple

t = (34, 45, 23, 12, 34, 45, 67, 89)
print(reversed(t)) # <reversed object at 0x000001F3C8B8C4C0> # Reversed object
print(tuple(reversed(t))) # (89, 67, 45, 34, 12, 23, 45, 34) # Tuple

# Tuple unpacking: Tuple unpacking is a feature in Python that allows you to assign the values of a tuple to multiple variables in a single line of code. This can be useful when you want to extract specific values from a tuple and assign them to separate variables for further processing. The syntax for tuple unpacking is to use parentheses to define the tuple and then use the assignment operator (=) to assign the values of the tuple to the variables.
t = (1, 2, 3)
a, b, c = t
print(a) # 1
print(b) # 2
print(c) # 3


# set in Python
# {}
# collection of unique elements in no particular order. It is a mutable data structure that allows you to store and manipulate a collection of elements. Sets are defined using curly braces {} or the
# unordered
# slicing : no
# mutable: yes
# indexing: no
# duplicate elements: no
# heterogeneous elements: yes

s = {1, 2, 3, 4, 5}
print(s) # {1, 2, 3, 4, 5}

s = set()
print(s) # set() # Empty set
print(type(s)) # <class 'set'>

"""
s = {1,2, "hello", 3.14, True, None, {"key": "value"}, (4, 5, 6), [1, 2, 3] , {1,2,1,3}} # Error: unhashable type: 'dict' and 'list' and 'set'
print(s)
"""
s = {2,3, "hello", 3.14, True, None, (4, 5, 6)}
print(s) # {2, 3, 'hello', 3.14, True, None, (4, 5, 6)}
s = {1,2, "hello", 3.14, True, None, (4, 5, 6)}
print(s) # {1, 2, 'hello', 3.14, None, (4, 5, 6), {1, 2, 3}}

s={1, 2, 3, 4, 5}
s.add(8) # {1, 2, 3, 4, 5, 8}
print(s) # {1, 2, 3, 4, 5, 8}
s.add(3) # {1, 2, 3, 4, 5, 8} # No effect as 3 is already present in the set
print(s) # {1, 2, 3, 4, 5, 8}
s.add(7) # {1, 2, 3, 4, 5, 7, 8}
print(s) # {1, 2, 3, 4, 5, 7, 8}


# pop() method: The pop() method is a built-in method in Python that is used to remove and return an arbitrary element from a set. It does not take any arguments and removes a random element from the set. If the set is empty, it raises a KeyError.
s = {1, 2, 3, 4, 5}
s.pop() # 1
print(s) # {2, 3, 4, 5}
# s.pop(3) # Error: pop() takes no arguments (1 given)

# update() method: The update() method is a built-in method in Python that is used to add multiple elements to a set. It takes an iterable as an argument and adds each element of the iterable to the set.
s.update([7, 8, 9]) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove() method: The remove() method is a built-in method in Python that is used to remove a specified element from a set. It takes one argument, which is the element to be removed, and removes it from the set. If the element is not found in the set, it raises a KeyError.
s = {1, 2, 3, 4, 5}
s.remove(3) # {1, 2, 4, 5}
print(s) # {1, 2, 4, 5}
# s.remove(6) # Error: KeyError: 6

# discard() method: The discard() method is a built-in method in Python that is used to remove a specified element from a set. It takes one argument, which is the element to be removed, and removes it from the set. If the element is not found in the set, it does nothing and does not raise an error.
s = {1, 2, 3, 4, 5}
s.discard(3) # {1, 2, 4, 5}
print(s) # {1, 2, 4, 5}

"""
# Difference between remove() and discard() methods: The main difference between the remove() and discard() methods is that the remove() method raises a KeyError if the specified element is not found in the set, while the discard() method does not raise an error and simply does nothing if the element is not found. Therefore, if you want to remove an element from a set and you are not sure if it exists in the set, it is safer to use the discard() method to avoid potential errors.
# Example:
s = {1, 2, 3, 4, 5}
s.remove(3) # {1, 2, 4, 5}
print(s) # {1, 2, 4, 5}
s.remove(6) # Error: KeyError: 6
s = {1, 2, 3, 4, 5}
s.discard(3) # {1, 2, 4, 5}
print(s) # {1, 2, 4, 5}
print(s.discard(6)) # None
"""

s1 = {1, 2, 3, 4, 5}
s1.clear() # set()
print(s1) # set()

s1 = {1, 2, 3, 4, 5}
s2 = s1.copy() # {1, 2, 3, 4, 5}
print(s1 is s2) # False

s1 = {1,2,3}
s2 = {3,4,5}
print(s1 | s2) # {1, 2, 3, 4, 5} # union
print(s1.union(s2)) # {1, 2, 3, 4, 5} # union
print(s1 & s2) # {3} # intersection
print(s1.intersection(s2)) # {3} # intersection

s1 = {1,2,3}
s2 = {3,4,5}
print(s1 - s2) # {1, 2} # difference
print(s1.difference(s2)) # {1, 2} # difference


# Helper function: A helper function is a function that is used to perform a specific task that is needed by another function. It is often used to break down a complex problem into smaller, more manageable parts. Helper functions are typically defined within the scope of the main function and are not intended to be called directly by the user. They are used to simplify the code and make it more readable and maintainable.
# Helper function is a function inside function.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

print(outer_function(5)(10)) # 15

def outer():
    print("This is the outer function.")
    def inner():  # Local function defined inside outer()
        print("This is the inner function.")


# outer() # This is the outer function.
# inner() # Error: NameError: name 'inner' is not defined
# outer(inner()) # This is the outer function. This is the inner function.

# Anonymous function: An anonymous function is a function that is defined without a name. In Python, anonymous functions are created using the lambda keyword. They are often used as a quick and simple way to define small functions that can be passed as arguments to other functions or used in functional programming constructs like map(), filter(), and reduce(). Lambda functions can take any number of arguments, but they can only have a single expression. The syntax for defining a lambda function is: lambda arguments: expression.
# anonymous function : lambda function : lambda arguments: expression
# function has no name

function = lambda x, y: x + y
print(function(5, 10)) # 15

# square(s)
sqr = lambda x: x ** 2
print(sqr(5)) # 25

print((lambda no: no + 1)(5)) # 6

ans = lambda no: no%2 ==0
print(ans(5)) # False
print(ans(6)) # True

ans = lambda no: "Even" if no%2 ==0 else "Odd"
print(ans(5)) # Odd
print(ans(6)) # Even