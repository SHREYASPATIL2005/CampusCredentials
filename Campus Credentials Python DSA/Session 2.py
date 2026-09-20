# for loop in python

from ast import List


for i in range(5):
    print(i)

# for(i=0; i<5; i++)
    print(i)

#for range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(1,5):
    print(i)

for i in range(10, 1):
    print(i)

#odd
for i in range(1,101):
    if i % 2 == 1:
        print(i, end=" ")

#even
for i in range(100,0,-1):
    if i % 2 == 0:
        print(i, end=" ")
print()

# table of 4
for i in range(1, 11):
    print("4 x",i,"=",4*i)

# sum of number (679)
sum = 0
for i in range(1,679):
    sum += i
print(sum)

#Palindrome
"""
no = input("Enter No. : ")
if no==no[::-1]:
    print("P")
else:
    print("NP")

#Palindrome
no = input("Enter No. : ") #"1234321"
rev=""
i=len(no)-1
while i>=0:  # Reverse Interation 6 to 0 = 7 digits
    rev+=no[i]
    i-=1
print(rev)
print("P" if no==rev else "NP") 
"""


# ******
for i in range(0,5):
    print("*", end="")

# ***
# ***
# ***
# ***
# ***

for i in range(0,5):
    for j in range(0,3):
        print("*", end="")
    print()  # New Line

for i in range(0,5):
    for j in range(0,3):
        print("1", end="")
    print()  # New Line

no=1
for i in range(0,5):
    for j in range(0,3):
        print(no, end="")
    print()  # New Line
    no+=1


no=1
for i in range(0,3):
    for j in range(0,3):
        print(no, end="")
        no+=1
    print()  # New Line
    
no=1
for i in range(0,3):
    for j in range(0,3):
        print(no, end="")
        no+=1
    print()  # New Line
    no = 1

#333
#222
#111
no=3
for i in range(0,3):
    for j in range(0,3):
        print(no, end="")
    print()  # New Line
    no-=1

#AAA
#BBB
#CCC
ch=65
for i in range(0,3):
    for j in range(0,3):
        print(chr(ch), end="")
    print()  # New Line
    ch = ch + 1

#AAA
#BBB
#CCC
ch='A'
for i in range(0,3):
    for j in range(0,3):
        print(ch, end="")
    print()  # New Line
    ch = chr(ord(ch) + 1)


#ABC
#ABC
#ABC
ch='A'
for i in range(0,3):
    for j in range(0,3):
        print(ch, end="")
        ch = chr(ord(ch) + 1)
    print()  # New Line
    ch = 'A'

#ABC
#DEF
#GHI
ch='A'
for i in range(0,3):
    for j in range(0,3):
        print(ch, end="")
        ch = chr(ord(ch) + 1)
    print()  # New Line


#CCC
#BBB
#AAA
ch='C'
for i in range(0,3):
    for j in range(0,3):
        print(ch, end="")
    print()  # New Line
    ch = chr(ord(ch) - 1)

# *
# **
# ***
# ****
# *****
noofstar = 1
for i in range(0,5):
    for j in range(0,noofstar):
        print("*", end="")
    print()  # New Line
    noofstar +=1
print()

# *****
# ****
# ***
# **
# *
noofstar = 5
for i in range(0,5):
    for j in range(0,noofstar):
        print("*", end="")
    print()  # New Line
    noofstar -=1

print()

# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
noofstar = 1
for i in range(0,6):
    for j in range(0,noofstar):
        print("*", end="")
    print()  # New Line
    noofstar +=1
noofstar = 5
for i in range(0,5):
    for j in range(0,noofstar):
        print("*", end="")
    print()  # New Line
    noofstar -=1

print()

#     *
#    **
#   ***
#  ****
# *****
noofstar = 1
sp=4
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    print()
    noofstar +=1
    sp -=1
print()


#*****
# ****
#  ***
#   **
#    *
noofstar = 5
sp=0
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    print()
    noofstar -=1
    sp +=1
print()

#    *
#   ***
#  *****
# *******
#*********

noofstar = 1
sp=4
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    for st in range(1,noofstar):
        print("*", end="")
    print()
    noofstar +=1
    sp -=1

print()

#*********
# *******
#  *****
#   ***
#    *

noofstar = 5
sp=0
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    for st in range(1,noofstar):
        print("*", end="")
    print()
    noofstar -=1
    sp +=1

#    *
#   ***
#  *****
# *******
#*********
#*********
# *******
#  *****
#   ***
#    *
noofstar = 1
sp=4
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    for st in range(1,noofstar):
        print("*", end="")
    print()
    noofstar +=1
    sp -=1
noofstar = 5
sp=0
for i in range(0,5):
    for j in range(0,sp):
        print(" ", end="")
    for k in range(0,noofstar):
        print("*", end="")
    for st in range(1,noofstar):
        print("*", end="")
    print()
    noofstar -=1
    sp +=1

#s1="HELLO GDSS"
#print(s1)

s1="hello"
s2="hello"
print(s1)
print(s2)
print(id(s1)) # Output: 2783219452304
print(id(s2)) # Output: 2783219452304

s1="hello"
s2="ABCD"
print(s1)
print(s2)
print(id(s1)) # Output: 2783219452304
print(id(s2)) # Output: 2479993425184

s1="hello"
s2="ABCD"
s3=s1+s2
print(s1)
print(s2)
print(s3)
print(id(s1)) # Output: 0 v2852906437008
print(id(s2)) # Output: 2852906437920
print(id(s3)) # Output: 2852906368944

# Immutable in nature
s1="hello"
print(s1)
print(id(s1)) # Output: 2852906437008
s1= s1 + "ABCD"
print(s1)
print(id(s1)) # Output: 2852906368944


# Indexing in String
s1 = "HELLO GDSS"
print(s1)
print(s1[0]) # H
print(s1[-10]) # H
print(s1[-1]) # S
print(s1[6]) # Space
print(s1[1]) # E

# Slicing in String
# Syntax: string[start:end:step]
s1 = "HELLO GDSS"
print(s1)
print(s1[0:5]) # HELLO
print(s1[6:10]) # GDSS
print(s1[2:-3]) # LLO G
print(s1[-8:-3]) # LLO G
print(s1[0:10]) # HELLO GDSS
print(s1[-10:-1]) # HELLO GDS
print(s1[-10:0]) # Empty String -10 = 0
print(s1[-10:9]) # HELLO GDS
print(s1[-10:10]) # HELLO GDSS
print(s1[0:10:2]) # HLOGS
print(s1[0:10:3]) # HLOGS
print(s1[0::2]) # HLOGS
print(s1[0::3]) # HOS
print(s1[::2]) # HLOGS
print(s1[9::-1]) # SSDG HELLO  # print(s1[9:0:-1]) X
print(s1[-1::-1]) # SSDG OLLEH
print(s1[-1:0:-2]) # SGLH


# String Methods
s1= "heLlo Students"
print(id(s1))
print(s1.upper()) # HELLO STUDENTS
print(s1) # heLlo Students
print(s1.lower()) # hello students
print(s1) # heLlo Students
print(s1.title()) # Hello Students
print(s1.capitalize()) # Hello students
print(s1.swapcase()) # HElLO sTUDENTS
print(s1.casefold()) # hello students -> Gives the most aggressive lowercasing, used for caseless matching
print(s1.count("e")) # 1
print(s1.count("t")) # 2
print(s1.count("T")) # 0
print(s1.lower().count("t")) # 2
print(s1.endswith("s")) # True
print(s1.endswith("S")) # False
print(s1.startswith("h")) # True
print(s1.startswith("H")) # False
print(s1.find("e")) # 1
print(s1.find("t")) # 8

s1 = "hi hi hi hi hellow how are u ?"
s1 = s1.replace("hi", "hello")
print(s1) # hello hello hello hello hellow how are u ?
s1 = "hi hi hi  Hi hellow how are u ?"
s1 = s1.replace("Hi", "hello")
print(s1) # hi hi hi  hello hellow how are u ?
s1 = s1.replace("hi", "hello",2)
print(s1) # hello hello hi  hello hellow how are u ?

s1 = "hello students how are you ? hi hi hi"
print(s1.find("s"))
print(s1.find("st"))
print(s1.find("h",4)) # 15
print(s1.find("h",16)) # 29
print(s1.find("h",16,20)) #-1

# string to list : split()
s1 = "hello"
s1 = s1.split()
print(s1) # ['hello']

s1 = "hello students welcome"
s1 = s1.split()
print(s1) # ['hello', 'students', 'welcome']

s1  = "hello,students,welcome"
s1 = s1.split(",")
print(s1) # ['hello', 'students', 'welcome']

s1  = "hello students welcome"
s1 = s1.split(",")
print(s1) # [hello students welcome] - No Split


# List to String : join()
l=['hello', 'students', 'welcome']
s1 = " ".join(l)
# s1 = "$".join(l)
print(s1) # hello students welcome


# strip() : Remove leading and trailing spaces
s1 = "       hello       "
print(s1.strip()) # hello
print(s1.lstrip()) # hello
print(s1.rstrip()) #        hello


"""
Centering a string
import string
s1 = "hello"
s1 = s1.center("#", 10)
print(s1) # ####hello###

s1 = "hello"
s1 = s1.center(10, "$")
print(s1) # ##hello### 
"""

s = "123456789"
print(s.isalnum()) # True

s = "ABC"
print(s.isalpha()) # True

s = "ABC123"
print(s.isalnum()) # True
print(s.isdigit()) # False
print(s.isalpha()) # False


s1 = "hello"
for i in s1:
    print(i, end=" ") # h e l l o

print()

s1 = "hello"
for i in range(0,len(s1)):
    print(i, end=" ") # 0 1 2 3 4
    print(s1[i], end=" ") # h e l l o

print()

s1 = "hello"
for i in range(len(s1)-1,-1,-1): # syntax: range(start, stop, step)
    print(i, end=" ") # 5 4 3 2 1
    print(s1[i], end=" ") # o l l e h

print()

# String Reverse using SWAP
s1 = "hello"
s1 = list(s1)
i = 0
j = len(s1)-1
while i < j:
    s1[i], s1[j] = s1[j], s1[i]
    i += 1
    j -= 1
print(s1) # ['o', 'l', 'l', 'e', 'h']
print("".join(s1)) # olleh

s1 = "hello"
s2 = ""
for i in range(len(s1)-1,-1,-1):
    s2 += s1[i]
print(s2) # olleh

# Length of String without using len()
s1 = "hello"
length = 0
for i in s1:
    length += 1
print(length) # 5

# Count Vowels in String
s1 = "hello"
vowels = "aeiouAEIOU"
vowels_count = 0
for i in s1:
    if i in vowels:
        vowels_count += 1
print(vowels_count) # 2

# Count Consonants in String
s1 = "hello"
consonants_count = 0
unique_chars = set(s1)  # To avoid counting duplicates
for i in s1:
    vowels = "aeiouAEIOU"
    if i not in vowels and i.isalpha():
        consonants_count += 1
print(consonants_count) # 3

# Count Characters in String
s1 = "hello"
count = 0
for i in s1:
    print(i, end=" ") # h e l l o
    count += 1
print(count) # 5

# Count spaces in String
s1 = "hello world"
count = 0
for i in s1:
    if i == " ":
        count += 1
print(count) # 1

# Palindrome Check
s1 = "AABCBAA"
Temp = s1
s1 = list(s1)
i = 0
j = len(s1)-1
while i < j:
    s1[i], s1[j] = s1[j], s1[i]
    i += 1
    j -= 1
print(s1) # ['o', 'l', 'l', 'e', 'h']
print("".join(s1)) # olleh
if Temp == "".join(s1):
    print("Palindrome")

# Check digit in string
s1 = "hello123"
digit_count = 0
for i in s1:
    if i.isdigit():
        digit_count += 1
print(digit_count) # 3

# Count special characters in string
s1 = "hello@123#"
special_count = 0
special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/~`"
for i in s1:
    if i in special_chars:
        special_count += 1
print(special_count) # 2


# Remove spaces using replace()
s1 = "hello world"
s1 = s1.replace(" ", "")
print(s1) # helloworld


# Remove spaces without using replace()
s1 = "hello world"
s1 = list(s1)
for i in range(len(s1)):
    if s1[i] == " ":
        s1[i] = ""
print("".join(s1)) # helloworld

print(s1) # helloworld

# Replace characters with different characters ( Accept both from user)
s1 = "hello"
old_char = input("Enter the character to be replaced: ")
new_char = input("Enter the new character: ")
s1 = s1.replace(old_char, new_char)
print(s1)

# function in python
# function is a block of code which is used to perform a specific task. It is reusable and can be called multiple times in a program.
# function implementation/definition
# funtion calling/invocation   -> function()

# Syntax of function in python
def function_name(parameters):
    # function body
    pass

#Types of function in python
# 1. functionwith no arguments and no return type
# 2. function with arguments and no return type
# 3. function with no arguments and return type
# 4. function with arguments and return type
# 5. function with default arguments

# def fun(empty): #noargument
# def fun1(a,b): #with argument

# 1. function with no arguments and no return type
def fun():
    print("Hello World")
    print("Hi")

fun() # function calling

"""
# 2. function with arguments and no return type
def add(a,b):
    c = a + b
    print(c)

# add(5, 10)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add(a,b)
"""


# 3. function with no arguments and return type
"""
def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = a + b
    return c

result = add()
print(result)
"""

# 4. function with arguments and return type
"""
def add(a,b):
    c = a + b
    return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a,b)
print(result)
"""

# 4. function with arguments and return type
def add(a:str,b:str,c:str) -> bool:
    return a + b + c

print(add(1,2,3)) # 6
print(add("1","2","3")) # 123

# 5. function with default arguments
def add(a=0,b=0):
    c = a + b
    return c
result = add(5,10)
print(result) # 15

result = add()
print(result) # 0


def display(name, age=18): # give value to all or give value to last parameter only or from right to left
    print("Name:", name)
    print("Age:", age)

display("Alice")  # Age will be 18
display("Bob", 25)  # Age will be 25

# print(add(5)) # 5

# function with variable argument
def fun(a):
    print(a)

fun(5)
# fun(5, 10) # TypeError: fun() takes 1 positional argument but 2 were given

def fun(*args):
    print(args) # tuple

# fun(5)
fun(5, 10) # (5, 10)
fun(5, 10, 15) # (5, 10, 15)

def fun(*a,b,c):
    print(a) # tuple
    print(b) # 20
    print(c) # 30

fun(10,20,30,b=20,c=30) # b and c must be passed by keyword.

def fun(a,b,*c):
    print(a)
    print(b)
    print(c)

fun(10,20,30,40) # a=10, b=20, c=(30, 40)

a,b,c = (10,20,30) # A starred target is not required when the sizes match.
print(a)
print(b)
print(c)

a,b,*c = (10,20,30,40) # Starred assignment collects the remaining values.
print(a) # 10
print(b) # 20
print(c) # (30, 40)





"""
"""

# DICTIONARY FOR ROMAN NUMBERS



