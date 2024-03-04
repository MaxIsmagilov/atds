#!/usr/bin/env python3

"""
adts.py
A collection of ADT classes
"""
__author__ = "Max Ismagilov"
__version__ = "2024-02-13"

class Stack:
    """This class creates a stack (wrapped around list)
    """
    
    def __init__(self) -> None:
        """constructor, takes no arguments
        """
        self.arr = []
        
    def push(self, value):
        """pushes to the stack
        """
        self.arr.append(value)
        
    def pop(self):
        """pops and returns the last value
        """
        try:
            return self.arr.pop(len(self.arr)-1)
        except:
            return None
    
    def peek(self):
        """peeks and returns the last value
        """
        try:
            return self.arr[len(self.arr)-1]
        except:
            return None
        
    def size(self):
        """returns the size of the stack
        """
        return len(self.arr)
    
    def is_empty(self):
        """returns whether this is empty
        """      
        return (self.size() == 0)
    
    def __repr__(self):
        return ("Stack has: [" + (self.arr.__repr__()) + "]")

class Queue:
    def __init__(self):
        self.arr = []
        
    def size(self):
        return len(self.arr)
        
    def enqueue(self, item):
        self.arr.append(item)
    
    def dequeue(self):
        return self.arr.pop(0)
        
    def is_empty(self):
        return len(self.arr) == 0
    
    def peek(self):
        return self.arr[0] 
    
    def __repr__(self):
        return ("Queue has: [*front*" + (self.arr.__repr__()) + "*end*]")
        
class Deque:
    def __init__(self) -> None:
        self.arr = []
        
    def add_front(self, item):
        self.arr.insert(0, item)
        
    def add_rear(self, item):
        self.arr.append(item)
        
    def remove_front(self):
        return self.arr.pop(0)
        
    def remove_rear(self):
        return self.arr.pop()
        
    def size(self):
        return len(self.arr)
    
    def is_empty(self):
        return len(self.arr) == 0

class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
        
    def __init__(self, data, next) -> None:
        self.data = data
        self.next = next
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, value):
        self.data = value
        
    def set_next(self, value):
        self.next = value
        
    def __repr__(self) -> str:
        return f"Node(data: {self.data}, next:{self.next})"
        
class UnorderedList:
    def __init__(self) -> None:
        self.head = None
    
    def add(self, item):
        if (self.head == None):
            self.head = Node(item, None)
        else:
            head_val = self.head
            self.head = Node(item, head_val)
            
    def remove(self, item):
        while (self.search(item)):
            self.remove_first(item)
            
    def remove_first(self, item):
        """
        removes JUST the first instance of an item

        """
        n = self.head
        if (self.head == None):
            return
        if (self.head.get_data() == item):
            self.head = self.head.get_next()
            return
        while (n.get_next() != None and n.get_next().get_data() != item):
            n = n.get_next()
        if (n.get_next() != None):
            n = n.set_next(n.get_next().get_next())
            return
        return
    
    
    def is_empty(self):
        return self.head == None
    
    def length(self):
        count = 0
        n = self.head
        while (n != None):
            count += 1
            n = n.get_next()
        return count
    
    def append(self, item):
        if self.head == None:
            self.add(item)
            return
        n = self.head
        while (n.get_next() != None):
            n = n.get_next()
        n.set_next(Node(item, None))
        
    def index(self, item):
        count = -1
        n = self.head
        while (n != None):
            count += 1
            if (n.get_data() == item):
                return count
            n = n.get_next()
        return -1
        
    def search(self, item):
        return self.index(item) != -1
    
    def insert(self, pos, item):
        n = self.head
        for i in range(0, pos):
            n = n.get_next()
        next = Node(n.get_data(), n.get_next())
        n.set_data(item)
        n.set_next(next)
        
    def pop(self):
        if self.head == None:
            return None
        if self.head.get_next() == None:
            val = self.head.get_data()
        n = self.head
        while (n.get_next().get_next() != None):
            n = n.get_next()
        
        val = n.get_next()
        n.set_next(None)
        return val 
    
    def pop(self, pos=-1):
        if pos == -1:
            pos = self.length()-1
        if pos == 0:
            self.head = self.head.get_next()
            return
        n = self.head
        for i in range(0, pos-1):
            n = n.get_next()
        val = n.get_next().get_data()
        n.set_next(n.get_next().get_next())
        return val
        
    def __repr__(self): # literally just Mr. White's method
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
        
class UnorderedListStack:
    def __init__(self) -> None:
        self.list = UnorderedList()
    
    def push(self, item):
        self.list.add(item)
    
    def pop(self):
        return self.list.pop(0)
    
    def peek(self):
        i = self.list.pop(0)
        self.list.add(i)
        return i;
    
    def size(self):
        return self.list.length()
    
    def is_empty(self):
        return self.list.length() == 0
            
    
            
            
            
