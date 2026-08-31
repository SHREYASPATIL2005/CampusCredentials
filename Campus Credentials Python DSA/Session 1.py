"""
roll = 10
# 1roll = 10 
print("Roll:", roll)
_roll = 20
# _roll = 20
print("_Roll:", _roll)
roll_2 = 30
# roll_2 = 30
print("Roll_2:", roll_2)

a = 10
b = 20 
print(a)
print(b)
a , b = 30 , 40
print(a)
print(b)

print(a, b) # This line prints the values of 'a' and 'b' after they have been reassigned to 30 and 40, respectively. The output will be "30 40".

name = input("Enter your name: ") # This line prompts the user to enter their name and stores it in the variable 'name'.
print("Hello, " + name + "!") # This line prints a greeting message that includes the user's name. For example, if the user enters "Shreyas", the output will be "Hello, Shreyas!".

a  = input("Enter number 1: " ) # This line prompts the user to enter a value and stores it in the variable 'a' as a string.
b = input("Enter number 2: ") # This line prompts the user to enter another value and stores it in the variable 'b' as a string.

# Typecasting is necessary because the input function returns a string, and we want to perform arithmetic operations on the values.
# a = int(input("Enter number 1: " )) # This line prompts the user to enter a value and stores it in the variable 'a' as an integer.
# b = int(input("Enter number 2: ")) # This line prompts the user to enter a value and stores it in the variable 'b' as an integer.

# Convert the string inputs to integers (OLD METHOD)
a = int(a)
b = int(b)

c = a + b
print("Addition is: ", c)
print("Addition is: ", +c)
print("Addition is: " +str(c)) # This line prints the sum of 'a' and 'b' (which are now 30 and 40) as a string. The output will be "Addition is: 70".

print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'int'> since it has been converted to an integer.
print(type(b)) # This line prints the data type of the variable 'b', which will also be <class 'int'> since it has been converted to an integer.

print("Addition of a and b is:", a + b) # This line calculates the sum of 'a' and 'b' (which are now 30 and 40) and prints the result. The output will be "Addition of a and b is: 70".


print("Hello")
print('Hii')

print('hello students "I am Trainer" Welcome') # This line prints a string that contains both single and double quotes. The output will be 'hello students "I am Trainer"'.
print("hello students 'I am Trainer' Welcome") # This line prints a string that contains both single and double quotes. The output will be "hello students 'I am Trainer'".
print('hello students \"I am Trainer\" Welcome') # This line prints a string that contains both single and double quotes. The output will be 'hello students "I am Trainer"'.

print("I' m Python Trainer") # This line prints a string that contains an apostrophe. The output will be "I' m Python Trainer".
print('I\' m Python Trainer') # This line prints a string that contains an apostrophe. The output will be "I' m Python Trainer".

# a,b = int(input("Enter value for a and b: "))  Throw Error because input() returns a string, and you cannot unpack a single integer into two variables. The correct way to get two integers from user input is to split the input string and convert each part to an integer separately.
#Error :  a,b = int(input("Enter value for a and b: ")).split() # This line prompts the user to enter two values separated by a space, converts them to integers, and assigns them to the variables 'a' and 'b'.
# print("Addition of a and b is:", a + b) # This line calculates the sum of 'a' and 'b' (which are now the two integers entered by the user) and prints the result. The output will be "Addition of a and b is: <sum>", where <sum> is the sum of the two integers entered by the user.

a, b = input("Enter value for a and b: ").split() # This line prompts the user to enter two values separated by a space and stores them as strings in the variables 'a' and 'b'.
# a, b = input("Enter value for a and b: ").strip(" ") # This line prompts the user to enter two values separated by a space and stores them as strings in the variables 'a' and 'b'.
a = int(a) # This line converts the string value of 'a' to an integer.
b = int(b)

print("Addition of a and b is:", a + b)

a, b = map(int, input("Enter value for a and b: ").split())
print("Addition of a and b is:", a + b)


a,b = int(input("Enter value of a: ")), int(input("Enter value of b: ")) # This line prompts the user to enter two values separately, converts them to integers, and assigns them to the variables 'a' and 'b'.
print("Addition of a and b is:", a + b) # This line calculates the sum of 'a' and 'b' (which are now the two integers entered by the user) and prints the result. The output will be "Addition of a and b is: <sum>", where <sum> is the sum of the two integers entered by the user.

#Arithmetic Operations
print(a%b) # This line calculates the remainder of 'a' divided by 'b' and prints the result. The output will be "<remainder>", where <remainder> is the result of the modulus operation.
print(a/b) # This line calculates the division of 'a' by 'b' and prints the result. The output will be "<division_result>", where <division_result> is the result of the division operation.
print(a//b) # This line calculates the floor division of 'a' by 'b' and prints the result. The output will be "<floor_division_result>", where <floor_division_result> is the result of the floor division operation.
print(a*b) # This line calculates the multiplication of 'a' and 'b' and prints the result. The output will be "<multiplication_result>", where <multiplication_result> is the result of the multiplication operation.
print(a**b) # This line calculates 'a' raised to the power of 'b' and prints the result. The output will be "<power_result>", where <power_result> is the result of the exponentiation operation.

# Relational Operators
print(a>b) # This line checks if 'a' is greater than 'b' and
print(a<b) # This line checks if 'a' is less than 'b' and prints the result as a boolean value (True or False).
print(a>=b) # This line checks if 'a' is greater than or equal to 'b' and prints the result as a boolean value (True or False).
print(a<=b) # This line checks if 'a' is less than or equal to
print(a==b) # This line checks if 'a' is equal to 'b' and prints the result as a boolean value (True or False).
print(a!=b) # This line checks if 'a' is not equal to 'b
"""
a = 10
b = 20
a -= b # This line subtracts the value of 'b' from 'a' and assigns the result back to 'a'. After this operation, 'a' will be -10.
a = a -b # This line subtracts the value of 'b' from 'a' and assigns the result back to 'a'. After this operation, 'a' will be -30.

print(a) # This line prints the current value of 'a', which is -30 after the subtraction operation.

a *= b # This line multiplies the value of 'a' by 'b' and assigns the result back to 'a'. After this operation, 'a' will be -600.
print(a) # This line prints the current value of 'a', which is -600 after the multiplication operation.
a /= b # This line divides the value of 'a' by 'b' and assigns the result back to 'a'. After this operation, 'a' will be -30.0.
print(a) # This line prints the current value of 'a', which is -30.0 after the division operation.
a **= b # This line raises the value of 'a' to the power of 'b' and assigns the result back to 'a'. After this operation, 'a' will be a very large negative number.
print(a) # This line prints the current value of 'a', which is a very large negative number after the exponentiation operation.

a = 20
b = 50
a //= b # This line performs floor division of 'a' by 'b' and assigns the result back to 'a'. After this operation, 'a' will be a large negative number.
print(a) # This line prints the current value of 'a', which is a large negative number after the floor division operation.

a %= b # This line calculates the remainder of 'a' divided by 'b' and assigns the result back to 'a'. After this operation, 'a' will be a negative number between 0 and -b.
print(a) # This line prints the current value of 'a', which is a negative number between 0 and -b after the modulus operation.

# Logical Operators
a = True
b = False
print(a and b) # This line performs a logical AND operation between 'a' and 'b' and prints the result. The output will be False since both operands are not True.
print(a or b) # This line performs a logical OR operation between 'a' and 'b' and prints the result. The output will be True since at least one of the operands is True.
print(not a) # This line performs a logical NOT operation on 'a' and prints the result. The output will be False since 'a' is True.
print(not b) # This line performs a logical NOT operation on 'b' and prints the result. The output will be True since 'b' is False.

print(1 and 1) # This line performs a logical AND operation between the two integers 1 and 1. Since both operands are non-zero (True), the result will be the second operand, which is 1.
print(1 and 0) # This line performs a logical AND operation between the two integers 1 and 0. Since the second operand is zero (False), the result will be 0.
print(0 and 1) # This line performs a logical AND operation between the two integers 0 and 1. Since the first operand is zero (False), the result will be 0.
print(0 and 0) # This line performs a logical AND operation between the two integers 0 and 0. Since both operands are zero (False), the result will be 0.

print(1 or 1) # This line performs a logical OR operation between the two integers 1 and 1. Since both operands are non-zero (True), the result will be the first operand, which is 1.
print(1 or 0) # This line performs a logical OR operation between the two integers 1 and 0. Since the first operand is non-zero (True), the result will be the first operand, which is 1.
print(0 or 1) # This line performs a logical OR operation between the two integers 0 and 1. Since the first operand is zero (False), the result will be the second operand, which is 1.
print(0 or 0) # This line performs a logical OR operation between the two integers 0 and 0. Since both operands are zero (False), the result will be 0.

print (10 and 23) # This line performs a logical AND operation between the two integers 10 and 23. In Python, any non-zero integer is considered True, so the result will be the second operand, which is 23.
print (10 or 23) # This line performs a logical OR operation between the two integers 10 and 23. In Python, any non-zero integer is considered True, so the result will be the first operand, which is 10.
print (0 and 23) # This line performs a logical AND operation between the two integers 0 and 23. Since the first operand is zero (False), the result will be 0.
print (0 or 23) # This line performs a logical OR operation between the two integers 0 and 23. Since the first operand is zero (False), the result will be the second operand, which is 23.
print (10 and 0) # This line performs a logical AND operation between the two integers 10 and 0. Since the second operand is zero (False), the result will be 0.
print (10 or 0) # This line performs a logical OR operation between the two integers 10 and 0. Since the first operand is non-zero (True), the result will be the first operand, which is 10.

print(not 10) # This line performs a logical NOT operation on the integer 10. In Python, any non-zero integer is considered True, so the result will be False.
print(not 0) # This line performs a logical NOT operation on the integer 0. In Python, zero is considered False, so the result will be True.
print(not 23) # This line performs a logical NOT operation on the integer 23. In Python, any non-zero integer is considered True, so the result will be False.
print(not -10) # This line performs a logical NOT operation on the integer -10. In Python, any non-zero integer is considered True, so the result will be False.

# Bitwise Operators
a = 10
b = 20
print(50 & 40) # This line performs a bitwise AND operation between the integers 50 and 40. The result will be 32, which is the bitwise AND of the two numbers.
print(50 | 40) # This line performs a bitwise OR operation between the integers 50 and 40. The result will be 58, which is the bitwise OR of the two numbers.
print(20^20) # This line performs a bitwise XOR operation between the integers 20 and 20. The result will be 0, which is the bitwise XOR of the two numbers.
print(20<<2) # This line performs a left shift operation on the integer 20 by 2 bits. The result will be 80, which is equivalent to multiplying 20 by 2 raised to the power of 2 (20 * 4).
print(20>>2) # This line performs a right shift operation on the integer 20 by 2 bits. The result will be 5, which is equivalent to dividing 20 by 2 raised to the power of 2 (20 / 4).

print(10^20) # This line performs a bitwise XOR operation between the integers 10 and 20. The result will be 30, which is the bitwise XOR of the two numbers.
print(~9) # This line performs a bitwise NOT operation on the integer 9. The result will be -10, which is the bitwise NOT of the number.
print(~-9) # This line performs a bitwise NOT operation on the integer -9. The result will be 8, which is the bitwise NOT of the number.

l = [10, 20, 30, 40, 50]
print(l) # This line prints the list 'l', which contains the integers 10, 20, 30, 40, and 50. The output will be "[10, 20, 30, 40, 50]".
print(type(l)) # This line prints the data type of the variable 'l', which will be <class 'list'> since it is a list.
print(50 in l) # This line checks if the integer 50 is present in the list 'l' and prints the result as a boolean value (True or False). The output will be True since 50 is an element of the list.
print(60 in l) # This line checks if the integer 60 is present in the list 'l' and prints the result as a boolean value (True or False). The output will be False since 60 is not an element of the list.
print(60 not in l) # This line checks if the integer 60 is not present in the list 'l' and prints the result as a boolean value (True or False). The output will be True since 60 is not an element of the list.
print(50 not in l) # This line checks if the integer 50 is not present in the list 'l' and prints the result as a boolean value (True or False). The output will be False since 50 is an element of the list.
print("hello" in l) # This line checks if the string "hello" is present in the list 'l' and prints the result as a boolean value (True or False). The output will be False since "hello" is not an element of the list.

# Comparison Operators
a = 10
b = 20

print(a > b) # This line checks if 'a' is greater than 'b' and prints the result as a boolean value (True or False). The output will be False since 10 is not greater than 20.
print(a < b) # This line checks if 'a' is less than 'b' and prints the result as a boolean value (True or False). The output will be True since 10 is less than 20.
print(a >= b) # This line checks if 'a' is greater than or equal to 'b' and prints the result as a boolean value (True or False). The output will be False since 10 is not greater than or equal to 20.
print(a <= b) # This line checks if 'a' is less than or equal to 'b' and prints the result as a boolean value (True or False). The output will be True since 10 is less than or equal to 20.
print(a == b) # This line checks if 'a' is equal to 'b' and prints the result as a boolean value (True or False). The output will be False since 10 is not equal to 20.
print(a != b) # This line checks if 'a' is not equal to 'b' and prints the result as a boolean value (True or False). The output will be True since 10 is not equal to 20.
print(a is b) # This line checks if 'a' and 'b' refer to the same object in memory and prints the result as a boolean value (True or False). The output will be False since 'a' and 'b' are different integers.
print(a is not b) # This line checks if 'a' and 'b' do not refer to the same object in memory and prints the result as a boolean value (True or False). The output will be True since 'a' and 'b' are different integers.
print(a is not 10) # This line checks if 'a' does not refer to the same object as the integer 10 in memory and prints the result as a boolean value (True or False). The output will be False since 'a' is equal to 10.
print(a is 10) # This line checks if 'a' refers to the same object as the integer 10 in memory and prints the result as a boolean value (True or False). The output will be True since 'a' is equal to 10.
print(a is not 20) # This line checks if 'a' does not refer to the same object as the integer 20 in memory and prints the result as a boolean value (True or False). The output will be True since 'a' is not equal to 20.
print(a is 20) # This line checks if 'a' refers to the same object as the integer 20 in memory and prints the result as a boolean value (True or False). The output will be False since 'a' is not equal to 20.


# Walrus Operator
# The walrus operator (:=) is used to assign a value to a variable as part of an expression. It allows you to both assign a value to a variable and use that value in the same expression.
print(a := 10) # This line uses the walrus operator to assign the value 10 to the variable 'a' and print it. The output will be 10.

a = 10
b = 20
if (c := a + b) > 20: # This line uses the walrus operator to assign the sum of 'a' and 'b' to the variable 'c' and check if 'c' is greater than 20 in the same expression.
    print(f"The sum of a and b is {c}, which is greater than 20.") # If the condition is true, this line prints the value of 'c' along with a message indicating that it is greater than 20.
else:
    print(f"The sum of a and b is {c}, which is not greater than 20.") # If the condition is false, this line prints the value of 'c' along with a message indicating that it is not greater than 20.

a = 10
b = 20
x = a if a > b else b # This line uses a conditional expression (ternary operator) to assign the greater of 'a' and 'b' to the variable 'x'. If 'a' is greater than 'b', 'x' will be assigned the value of 'a'; otherwise, it will be assigned the value of 'b'.
print(f"The greater value between a and b is {x}.") # This line prints the value of 'x' along with a message indicating that it is the greater value between 'a' and 'b'.

# a=10
# b=20
print(x := "a is greater" if (a:=100) >(b:=20) else "b is greater")

import keyword
print(keyword.kwlist) # This line imports the 'keyword' module and prints the list of all reserved keywords in Python. The output will be a list of strings representing the keywords, such as ['False', 'None', 'True', 'and', 'as', 'assert', ...].

"""['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']"""

a = 135
rev = 0
sum = 0
while a > 0:
    rem = a % 10  # Gives last digit
    sum += rem # For addition
    print(rem)
    rev = rev * 10 + rem # Adds last digit to its correct place
    a = a // 10 # Removes last digit
    print(a)
    print(rev)

print("Sum of digits:", sum)
print("Reverse : " , rev)



# Comments :
 # Single line comment 
#  """ docstring """
""" docstring """
print(__doc__) # This line prints the docstring of the current module, which is the string enclosed in triple quotes at the beginning of the file. The output will be the content of the docstring, which provides information about the module.

def fun():
    """This is a docstring for the function 'fun'."""
    print("This is a function.")
    # Comment
    print("Hii")

print(fun.__doc__) # This line prints the docstring of the function 'fun', which is the string enclosed in triple quotes immediately after the function definition. The output will be "This is a docstring for the function 'fun'.".


# Data Types in Python

# In pyhton Integer is immutable data type. It means once we assign a value to an integer variable, we cannot change that value. If we try to change the value of an integer variable, a new integer object will be created in memory and the variable will point to that new object.
a = 10 # Integer
print(a) # This line prints the value of the variable 'a', which is 10.
print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'int'> since it is an integer.
b = 10.5 # Float
print(b) # This line prints the value of the variable 'b', which is 10.5.
print(type(b)) # This line prints the data type of the variable 'b', which will be <class 'float'> since it is a float.

# Scientific notation
# 2*10^3 = 2*10*10*10 = 2000

a = 3 + 4j # Complex number
print(a) # This line prints the value of the variable 'a', which is a complex number (3 + 4j).
print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'complex'> since it is a complex number.
print(a.real) # This line prints the real part of the complex number 'a', which is 3.0.
print(a.imag) # This line prints the imaginary part of the complex number 'a', which is 4.0.

s = "Hello, World!" # String
print(s) # This line prints the value of the variable 's', which is the string "Hello, World!".
print(type(s)) # This line prints the data type of the variable 's', which will be <class 'str'> since it is a string.

l = [1, 2, 3, 4, 5] # List # List is mutable data type. It means we can change the value of a list variable after it has been created. We can add, remove, or modify elements in a list without creating a new list object.
print(l) # This line prints the value of the variable 'l', which is a list containing the integers 1, 2, 3, 4, and 5.
print(type(l)) # This line prints the data type of the variable 'l', which will be <class 'list'> since it is a list.


t = (1, 2, 3, 4, 5) # Tuple

print(t) # This line prints the value of the variable 't', which is a tuple containing the integers 1, 2, 3, 4, and 5.
print(type(t)) # This line prints the data type of the variable 't', which will be <class 'tuple'> since it is a tuple.

print(t) # This line prints the value of the variable 't', which is a tuple containing the integers 1, 2, 3, 4, and 5.
print(type(t)) # This line prints the data type of the variable 't', which will be <class 'tuple'> since it is a tuple.
print(t[0]) # This line prints the first element of the tuple 't', which is 1.
print(t[-1]) # This line prints the last element of the tuple 't', which is 5.

a = 10, 20 , 30 # Tuple
print(a) # This line prints the value of the variable 'a', which is a tuple containing the integers 10, 20, and 30. The output will be "(10, 20, 30)".
print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'tuple'> since it is a tuple.

# a, b = 10, 20, 30 # Tuple unpacking # Error: too many values to unpack (expected 2) because there are three values on the right side of the assignment, but only two variables on the left side. To fix this, you can either add a third variable to unpack the third value or remove one of the values from the right side.
# print(a) # This line prints the value of the variable 'a', which is 10
# print(b) # This line prints the value of the variable 'b', which is 20. The output will be "20". Note that the third value (30) is not assigned to any variable and is ignored.
# print(c) # This line prints the value of the variable 'c', which is 30. The output will be "30".

range_obj = range(1, 10) # Range
# Range Syntax: range(start, stop, step)
print(range_obj) # This line prints the value of the variable 'range_obj', which is a range object representing the sequence of integers from 1 to 9 (inclusive of 1 and exclusive of 10).
print(type(range_obj)) # This line prints the data type of the variable 'range_obj', which will be <class 'range'> since it is a range object.

range_obj2 = range(1, 10, 2) # Range with step
print(range_obj2) # This line prints the value of the variable 'range_obj2', which is a range object representing the sequence of integers from 1 to 9 (inclusive of 1 and exclusive of 10) with a step of 2. The output will be "range(1, 10, 2)".
print(type(range_obj2)) # This line prints the data type of the variable 'range_obj2', which will be <class 'range'> since it is a range object.


#  Difference between Array and List in Python
# 1. Array is a collection of elements of the same data type, whereas List can contain elements of different data types.
# 2. Extending size of Array is not possible, whereas List can be dynamically resized.
# 3. Array is more efficient in terms of memory and performance, especially for large datasets, whereas List is more flexible and easier to use for general-purpose programming.
# 4. Array is implemented in Python using the 'array' module, whereas List is a built-in data type in Python.
# 5. Array supports fewer operations and methods compared to List, which has a rich set of built-in methods for manipulation and processing.


# SET
s = {1, 2, 3, 4, 5} # Set # mutable , unordered collection of unique elements ( no duplicates allowed)
print(s) # This line prints the value of the variable 's', which is a set containing the integers 1, 2, 3, 4, and 5. The output will be "{1, 2, 3, 4, 5}".
print(type(s)) # This line prints the data type of the variable 's', which will be <class 'set'> since it is a set.

s = frozenet = frozenset([1, 2, 3, 4, 5]) # Frozen Set # immutable , unordered collection of unique elements ( no duplicates allowed)
print(s) # This line prints the value of the variable 's', which is a frozenset containing the integers 1, 2, 3, 4, and 5. The output will be "frozenset({1, 2, 3, 4, 5})".
print(type(s)) # This line prints the data type of the variable 's', which will be <class 'frozenset'> since it is a frozenset.

# Mapping Type
d = {"name": "Shreyas", "age": 25, "city": "Pune"} # Dictionary # mutable , unordered collection of key-value pairs
print(d) # This line prints the value of the variable 'd', which is a dictionary containing the keys "name", "age", and "city" with their corresponding values. The output will be "{'name': 'Shreyas', 'age': 25, 'city': 'Pune'}".
print(type(d)) # This line prints the data type of the variable 'd', which will be <class 'dict'> since it is a dictionary.

# Boolean
a = True # Boolean
b = False # Boolean
print(a) # This line prints the value of the variable 'a', which is True.
print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'bool'> since it is a boolean.
print(b) # This line prints the value of the variable 'b', which is False.
print(type(b)) # This line prints the data type of the variable 'b', which will be <class 'bool'> since it is a boolean.

# Binary 
b = b'hello' # Binary
print(b) # This line prints the value of the variable 'b', which is a bytes object representing the string "hello" in binary format. The output will be "b'hello'".
print(type(b)) # This line prints the data type of the variable 'b', which will be <class 'bytes'> since it is a bytes object.

x = bytes([104, 101, 108, 108, 111]) # Bytes
print(x) # This line prints the value of the variable 'x', which is a bytes object representing the string "hello" in binary format. The output will be "b'hello'".
print(type(x)) # This line prints the data type of the variable 'x', which will be <class 'bytes'> since it is a bytes object.

b = bytearray(b'hello') # Bytearray
print(b) # This line prints the value of the variable 'b', which is a bytearray object representing the string "hello" in binary format. The output will be "bytearray(b'hello')".
print(type(b)) # This line prints the data type of the variable 'b', which will be <class 'bytearray'> since it is a bytearray object.


# None Type
a = None # None Type
print(a) # This line prints the value of the variable 'a', which is None.
print(type(a)) # This line prints the data type of the variable 'a', which will be <class 'NoneType'> since it is a NoneType.


a = 10
b = 20
c = 30
# Conditional Statements
if(a>b and a>c):
    d = a
elif(b>c):
    d = b
else:
    d = c
print(d)

# Ternaray Operator
a = 10
b = 20
c = 30
d = a if a > b and a > c else b if b > c else c
print(d)

n = 15
if n % 3 == 0:
    if n % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    if n % 5 == 0:
        print("Buzz")
    else:
        print("None")


# While Loop
n = 5
while n > 0:
    print(n)
    n -= 1
    if n == 0:
        print("Done")

i = 1
while i <= 5:
    print("hii")
    i += 1
else:
    print("Byee")

# Do-While loop
