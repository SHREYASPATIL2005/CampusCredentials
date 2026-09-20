# =====================================================================
# SESSION 5: OOP CONCEPTS & SINGLY LINKED LIST
# =====================================================================

# ---------------------------------------------------------------------
# 1. INHERITANCE (Single & Hierarchical)
# ---------------------------------------------------------------------
# Base class: defines common attributes for any person
class Person:
    def __init__(self, name, age): #self is used to refer to the instance of the class itself.
                                   #This is the constructor of the class. It is called when an object of the class is created.
        self.name = name
        self.age = age
        # print(name,age)

# Person("Shreyas",20)

# Derived class 1: Student inherits Person (Single Inheritance)
class Student(Person):
    def __init__(self, name, age, roll, s1, s2, s3):
        super().__init__(name, age)  # super() calls parent class's method
                                     # Reuses Person.__init__ for name & age
        self.roll = roll
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def displayS(self):
        print(self.name)
        print(self.age)
        print(self.roll)
        total = self.s1 + self.s2 + self.s3
        print("Total:", total)
        per = total / 3
        print("Percentage:", per)


# Derived class 2: Teacher also inherits Person (Hierarchical Inheritance)
class Teacher(Person):
    def __init__(self, name, age, id, sal, dept):
        super().__init__(name, age)  # Reuses Person.__init__
        self.id = id
        self.sal = sal
        self.dept = dept

    def displayT(self):
        print(self.name)
        print(self.age)
        print(self.id)
        print(self.sal)
        print(self.dept)


s = Student("rahul", 20, 1, 89, 76, 87)
s.displayS()

t = Teacher("Mr.Patil", 45, 101, 500000, "IT")
t.displayT()


# ---------------------------------------------------------------------
# 2. POLYMORPHISM
# ---------------------------------------------------------------------

# 2.1 Method Overloading limitation in Python:
# In Python, defining a method again OVERWRITES the previous definition.
class Ex:
    def add(self, a, b):
        print("addition of 2 nos is ", a + b)

    # Overwrites the previous add(self, a, b)
    def add(self, a, b, c):
        print("addition of 3 nos is ", a + b + c)

e = Ex()
e.add(1, 2, 4)  # Works: matches latest definition (3 arguments)
# e.add(1, 2)   # Fails: TypeError (Python does not support C++/Java style overloading)


# 2.2 Subclass Method Overriding:
class A:
    def add(self, a, b):
        print("addition of 2 nos is ", a + b)


class B(A):
    # Overrides parent's add() with a 3-argument version
    def add(self, x, y, z):
        print("addition of 3 nos is ", x + y + z)


a = A()
a.add(1, 2) # Output: addition of 2 nos is 3
# a.add(1, 2, 3) # Output: TypeError

b = B()
b.add(11, 2, 3)  # Calls B's add()
# b.add(11, 2)   # Fails: B's definition requires 3 arguments


# 2.3 Constructor Overloading:
# The 2nd __init__ overwrites the 1st; only the latest constructor exists.
class A_InitDemo:
    def __init__(self):
        print("from default constructor")

    def __init__(self, msg):
        print(msg, "Students..")


# a1 = A_InitDemo()        # Fails: requires 'msg' argument
a2 = A_InitDemo("welcome")  # Works: calls latest __init__
# output: welcome Students..


# Each object instantiation runs __init__ with provided argument
class A_Param:
    def __init__(self, a):
        print("hiii", a)


a1 = A_Param(12) # output: hiii 12 # This is object creation and constructor is called
a2 = A_Param(34) # output: hiii 34 # This is object creation and constructor is called
A_Param(1)     # output: hiii 1 # This is method calling not object creation # why ? -> because  no variable is assigned to the object. It just creates a temporary object and immediately calls the constructor with the given argument. Since this temporary object is not assigned to any variable, it gets garbage collected immediately after the constructor call completes.



# 2.4 Achieving Method Overloading via Default Arguments (Pythonic way):
class A_Default:
    def add(self, a, b, c=None):
        if c is None:
            print("addition of 2 nos ", a + b)
        else:
            print("addition of 3 nos ", a + b + c)


a_calc = A_Default()
a_calc.add(1, 2, 4)  # 3 args -> branch: a + b + c
a_calc.add(1, 2)     # 2 args -> branch: a + b


# 2.5 Method Overriding (Runtime Polymorphism):
# Child method replaces parent method when invoked on a child instance.
class ParentCar:
    def car(self):
        print("Maruti car..")


class ChildCar(ParentCar):
    def car(self):
        print("BMW...")  # Overrides parent implementation


b1 = ChildCar()
b2 = ParentCar()    
b1.car()  # Output: BMW...
b2.car() # Output: Maruti car...


# ---------------------------------------------------------------------
# 3. ENCAPSULATION (Data Hiding)
# ---------------------------------------------------------------------
# Double underscore '__' makes attributes private via name-mangling.
class Bank:
    def __init__(self, bal):
        self.__bal = bal  # Private variable; inaccessible directly as b.__bal

    def deposit(self, amt):
        self.__bal += amt
        print(amt, "successfully deposited..")

    def withdraw(self, amt):
        # Original condition rejected withdrawing the exact balance:
        # if self.__bal <= amt:
        if amt > self.__bal:
            print("Insufficient balance")
        else:
            self.__bal -= amt
            print(amt, "is withdrawn...")

    def getbal(self):
        print("Balance:", self.__bal)  # Public getter to safely read private data


b = Bank(10000)
b.deposit(1000)
b.getbal()
b.withdraw(4000)
b.getbal()
# print(b.__bal)  # Raises AttributeError: private variable hidden from outside


# ---------------------------------------------------------------------
# 4. ABSTRACTION
# ---------------------------------------------------------------------
# ABC module enforces abstract structure; child classes MUST implement @abstractmethods.
from abc import ABC, abstractmethod

# The original file imported requests only for an unused name:
# from requests import head

class Boss(ABC):
    @abstractmethod
    def Task(self):
        pass  # Abstract method: must be defined in child class

    def sal(self):
        print("sal credited")  # Concrete method: inherited directly


class Emp(Boss):
    def Task(self):
        print("task implemented")  # Implements required abstract method


e = Emp() # Creating an object of the class Emp which is derived from Boss (Abstract Class)
e.sal() # output: sal credited # Calling the concrete method from the parent class Boss
e.Task() # output: task implemented # Calling the abstract method from the child class Emp


# ---------------------------------------------------------------------
# 5. LINKED LIST: INTRO & MANUAL LINKING
# ---------------------------------------------------------------------
# A Node stores data and a pointer (reference) to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to next node, initially None


# Manual linking: [10] -> [20] -> [30] -> [40] -> None
start = Node(10)
start.next = Node(20)
start.next.next = Node(30)
start.next.next.next = Node(40)

# Manual traversal
print(start.data, end="-->")
print(start.next.data, end="-->")
print(start.next.next.data, end="-->")
print(start.next.next.next.data, end="-->None\n")


# ---------------------------------------------------------------------
# 6. COMPLETE SINGLY LINKED LIST IMPLEMENTATION
# ---------------------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.start = None  # Head pointer; None indicates empty list

    def createNode(self, val=None):
        # Creates a node using passed value or user input
        data = val if val is not None else int(input("Enter data: "))
        return Node(data)

    # Insert at Head: O(1) time
    def insertatfirst(self, val=None):
        if self.start is None:
            self.start = self.createNode(val)
        else:
            temp = self.createNode(val)
            temp.next = self.start  # New node points to existing head
            self.start = temp       # Head moves to new node

    # Insert at Tail: O(n) time
    def insertatlast(self, val=None):
        if self.start is None:
            self.start = self.createNode(val)
        else:
            s = self.start
            while s.next is not None:  # Traverse to last node
                s = s.next
            s.next = self.createNode(val)  # Attach at end

    # Insert at 1-based index: O(n) time
    def insertAtindex(self, index, val=None):
        if index < 1:
            print("invalid index")
        elif index == 1:
            return self.insertatfirst(val)
        else:
            s = self.start
            for i in range(1, index - 1):  # Reach (index - 1)th node
                if s is None or s.next is None:
                    print("index out of bounds")
                    return
                s = s.next
            temp = self.createNode(val)
            temp.next = s.next
            s.next = temp

    # Delete Head node: O(1) time
    def deletefromfirst(self):
        if self.start is None:
            print("no node to delete")
        else:
            s = self.start
            self.start = self.start.next  # Move head to 2nd node
            s.next = None                 # Disconnect old head

    # Delete Tail node: O(n) time
    def deletefromlast(self):
        if self.start is None:
            print("no node to delete")
        elif self.start.next is None:
            self.start = None  # Single node case
        else:
            s = self.start
            while s.next.next is not None:  # Stop at 2nd-to-last node
                s = s.next
            s.next = None  # Disconnect last node

    # Delete at 1-based index: O(n) time
    def deleteAtindex(self, index):
        if index < 1:
            print("invalid index")
        elif index == 1:
            return self.deletefromfirst()
        else:
            s = self.start
            for i in range(1, index - 1):  # Reach (index - 1)th node
                if s is None or s.next is None:
                    print("index out of bounds")
                    return
                s = s.next
            if s.next is not None:
                target = s.next
                s.next = s.next.next  # Bypass target node
                target.next = None

    # Traverse & print all nodes: O(n) time
    def displayNode(self):
        if self.start is None:
            print("no node available to display")
        else:
            s = self.start
            while s is not None:
                print(s.data, end="-->")
                s = s.next
            print("None")

    def countnodes(self):
        s=self.start
        count=0
        while s is not None:
            count+=1
            s=s.next
        return count

    def minNode(self):
        if self.start is None:
            return None
        s=self.start
        minimum=s.data
        while s is not None:
            if s.data < minimum:
                minimum = s.data
            s=s.next
        return minimum

    def maxNode(self):
        if self.start is None:
            return None
        s=self.start
        maximum=s.data
        while s is not None:
            if s.data > maximum:
                maximum = s.data
            s=s.next
        return maximum
    
    def secondlargest(self):
        if self.start is None:
            return None
        s=self.start
        secondmax=None
        maximum=s.data
        while s is not None:
            if s.data > maximum:
                secondmax = maximum
                maximum = s.data
            elif s.data != maximum and (secondmax is None or s.data > secondmax):
                secondmax = s.data
            s=s.next
        return secondmax
    
    def reverselinkedlist(self):
        prev=None
        current=self.start
        while current is not None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.start=prev

    def evennodecount(self):
        s=self.start
        evencount=0
        while s is not None:
            if s.data % 2 == 0:
                evencount+=1
            s=s.next
        return evencount

    def oddnodecount(self):
        s=self.start
        oddcount=0
        while s is not None:
            if s.data % 2 != 0:
                oddcount+=1
            s=s.next
        return oddcount

    def midNode(self):
        # The slow pointer reaches the middle when the fast pointer reaches the end.
        slow = self.start
        fast = self.start
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# ---------------------------------------------------------------------
# LINKED LIST TESTING
# ---------------------------------------------------------------------
l = LinkedList()

# Insert at first: 40 -> 30 -> 20 -> 10
l.insertatfirst(40)
l.insertatfirst(30)
l.insertatfirst(20)
l.insertatfirst(10)
l.displayNode()  # 10-->20-->30-->40-->None

# Insert at last: adds 50, 60, 70, 80
l.insertatlast(50)
l.insertatlast(60)
l.insertatlast(70)
l.insertatlast(80)
l.displayNode()  # 10-->20-->30-->40-->50-->60-->70-->80-->None

# Delete operations:
l.deletefromfirst()  # Removes 10
l.displayNode()

l.deletefromlast()   # Removes 80
l.displayNode()

# Index operations:
l.insertAtindex(3, 999)  # Inserts 999 at position 3
l.displayNode()

l.deleteAtindex(3)       # Removes element at position 3
l.displayNode()

print("Total nodes:", l.countnodes())  # Count nodes in list
print("Minimum node value:", l.minNode())  # Find min value
print("Maximum node value:", l.maxNode())  # Find max value
print("Second largest node value:", l.secondlargest())  # Find second largest value
print("Reversing linked list...")
l.reverselinkedlist()  # Reverse the linked list
l.displayNode()  # Display reversed list
print("Even nodes:", l.evennodecount())  # Count even nodes
l.insertatlast(11)  # Add an odd node for testing

l.displayNode()  # Display list after adding 11
print("Odd nodes:", l.oddnodecount())  # Count odd nodes