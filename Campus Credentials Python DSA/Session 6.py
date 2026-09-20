"""
def deleteAtindex(self,index):
        if index < 1:
            print("invalid index")
        elif index == 1:
            return self.deletefromfirst()
        elif index > 1:
            s=self.start
            for i in range(1,index-1):
                if s is None or s.next is None:
                    print("index out bounds")
                s=s.next
            s1=s.next
            if s.next is not None:
                s.next=s.next.next
            if s.next is not None:
                s1.next=None


# To count number of nodes in linked list
def countnodes(self):
        s=self.start
        count=0
        while s is not None:
            count+=1
            s=s.next
        return count

def minNode(self):
        s=self.start
        min=s.data
        while s is not None:
            if s.data < min:
                min = s.data
            s=s.next
        return min

def maxNode(self):
        s=self.start
        max=s.data
        while s is not None:
            if s.data > max:
                max = s.data
            s=s.next
        return max

def secondlargest(self):
        s=self.start
        secondmax=None
        max=s.data
        while s is not None:
            if s.data > max:
                secondmax = max
                max = s.data                
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
"""
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
"""
"""
# Doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None

    def createNode(Self):
        data = int(input("Enter data for the node: "))
        return Node(data)

    def insertNodeatFirst(self):
        if self.start == None:
            self.start = self.createNode()
        else:
            temp = self.createNode()
            temp.next = self.start
            self.start = temp
            self.start.next.prev = self.start

    def insertNodeatLast(self):
        if self.start == None:
            self.start = self.createNode()
        else:
            s = self.start
            while s.next is not None:
                s = s.next
            temp = self.createNode()
            s.next = temp
            temp.prev = s
            temp.next = None

    def deleteNodeatFirst(self):
        if self.start == None:
            print("List is empty")
        else:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def deleteNodeatLast(self):
        if self.start == None:
            print("List is empty")
        else:
            s = self.start
            while s.next is not None:
                s = s.next
            if s.prev is not None:
                s.prev.next = None
            else:
                self.start = None
            
    def displayNode(self):
        if self.start == None:
            print("List is empty")
        else:
            s = self.start
            while s is not None:
                print(s.data, end=" ")
                s = s.next
            print()

    def reverseNode(self):
        if self.start == None:
            print("List is empty")
        else:
            s = self.start
            while s.next is not None:
                s = s.next
            while s is not None:
                print(s.data, end=" ")
                s = s.prev
            print()

d = DoublyLinkedList()
d.insertNodeatFirst()
d.insertNodeatFirst()
d.insertNodeatFirst()
d.insertNodeatLast()
d.insertNodeatLast()

d.reverseNode()
d.displayNode()
"""
"""
class Node:
    def __init__(self, data):
        self.data = data

class CircularLinkedList:
    def createNode (self):
        data = int(input("Enter data for the node: "))
        return Node(data)

    def insertNodeatFirst(self):
        if self.start == None:
            self.start = self.createNode()
            self.start.next = self.start
        else:
            temp = self.createNode()
            temp.next = self.start
            s = self.start
            while s.next != self.start:
                s = s.next
            s.next = temp
            self.start = temp

    def displayNode(self):
        if self.start == None:
            print("List is empty")
        else:
            s = self.start
            while True: # s.next != self.start:
                print(s.data, end=" ")
                s = s.next
                if s == self.start:
                    break
            print()

d = CircularLinkedList()
d.insertNodeatFirst()
d.insertNodeatFirst()
d.insertNodeatFirst()
d.displayNode()
"""
"""
#Stack using linked list
class Stack:
    def __init__ (self,cap):
        self.stack = [None]*cap
        self.top = -1
        self.start = None
        self.cap = cap

    def push(self,data):
        if self.isfull():
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data
            print(f"{data} pushed to stack")

    def pop(self):
        if self.isEmpty():
            print("\n Stack is empty")
        else:
             x = self.stack[self.top]
             self.top -= 1
             return x

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack[self.top]


    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stack[self.top]

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()

# When array is Fixed size , we can use isEmpty and isFull methods to check if stack is empty or full
# When array is dynamic size , we can use isEmpty method to check if stack is empty or not but we cannot use isFull method to check if stack is full or not because stack can grow dynamically
    def isEmpty(self):
        return self.top == -1

    
    def isfull(self): #pd is your pandas import alias ( import pandas as pd) 
        import pandas as pd 
        return self.top == self.cap - 1

s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display()
s.pop()
s.display()
print(s.peek())
s.display()

class StackusingQueue:
    def __init__(self):
        self.que = []

    def push(self,data):
        self.que.append(data)
        print(f"{data} pushed to stack")
        for i in range(len(self.que)-1):
            self.que.append(self.que.pop(0))

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.que.pop(0)

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            for i in self.que:
                print(i, end=" ")
            print()

s = StackusingQueue()
s.push(10)
s.push(20)
s.push(30)
s.display()
print(s.pop())
s.display()
"""
# Queue : 
# Linear data structure
# It follows principle : first in first out (FIFO)

# Operations on Queue:
# 1. Enqueue : add an element to the end of the queue
# 2. Dequeue : remove an element from the front of the queue
# 3. Peek : get the front element of the queue without removing it
# isfull : check if the queue is full
# isEmpty : check if the queue is empty

# Implementation:
# 1. Using list/array : Insert at rear and delete at front
# 2. Using linked list : Insert at rear and delete from last
# 3. Using two stacks : Implement queue operations using two stacks

# Types of Queue:
# General Queue : Insert at rear and delete from front
# Circular Queue : Insert at rear and delete from front, but when rear reaches end of array
# Priority Queue : Each element has a priority, and the element with the highest priority is served first
# Deque : Double ended queue, where insertion and deletion can be done from both ends


# queue using list/array
#queue using list(fixed size)
"""
class Queue:
    def __init__(self,cap):
        self.cap=cap 
        self.que=[None]*cap
        self.front=-1
        self.rear=-1
        
    def enqueue(self,data):
        if self.isfull():
            print("queue is full")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.que[self.rear]=data
            print(data,"is inserted..")
        else:
            self.rear+=1
            self.que[self.rear]=data
            print(data,"is inserted..")        
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            x=self.que[self.front]
            self.que[self.front]=None
            print(x,"is deleted")
            self.front+=1
            
    def isfull(self):
        return self.rear==self.cap-1;
    
    def isEmpty(self):
        return self.front==-1;
    
    def display(self):
        print(self.que)
    
q=Queue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.display()
q.enqueue(60)
q.dequeue()
q.dequeue()
q.display()
q.enqueue(70)
q.display()
"""
class CQueue:
    def __init__(self,cap):
        if cap <= 0:
            raise ValueError("Queue capacity must be positive")
        self.cap=cap 
        self.que=[None]*cap
        self.front=-1
        self.rear=-1
        
    def enqueue(self,data):
        if self.isfull():
            print("queue is full")
        elif self.front==-1:
            self.front=0
            self.rear=0
            self.que[self.rear]=data
            print(data,"is inserted..")
        else:
            # Original code could run past the end after dequeuing:
            # self.rear += 1
            # Wrap the rear pointer so dequeued slots can be reused.
            self.rear=(self.rear+1)%self.cap
            self.que[self.rear]=data
            print(data,"is inserted..")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            x=self.que[self.front]
            self.que[self.front]=None
            print(x,"is deleted")
            if self.front==self.rear:
                self.front=-1
                self.rear=-1
            else:
                self.front=(self.front+1)%self.cap        


    def isfull(self):
        return (self.rear+1)%self.cap==self.front;

    def isEmpty(self):
        return self.front==-1;

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            i=self.front
            while True:
                print(self.que[i],end=" ")
                if i==self.rear:
                    break
                i=(i+1)%self.cap
            print()

c = CQueue(5)
c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.enqueue(50)
c.display()
c.enqueue(60)
c.display()
print(c.isfull())
c.dequeue()
c.dequeue()
c.display()
print(c.isEmpty())
print(c.isfull())

# PQ
class PQ:
    def __init__(self):
        self.pque=[]
        
    def enqueue(self,data,pr):
        self.pque.append((pr,data))
        self.pque.sort(key=lambda x:x[0])

    def dequeue(self):
        if not self.pque:
            return None
        return self.pque.pop(0)[1]

    def peek(self):
        if not self.pque:
            return None
        return self.pque[0][1]
        
    def display(self):
        print(self.pque)
        
p=PQ()
p.enqueue(30,4)
p.enqueue(280,2)
p.enqueue(31,1)
p.enqueue(45,2)
p.enqueue(43,5)
p.display()