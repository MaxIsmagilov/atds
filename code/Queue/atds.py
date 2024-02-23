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



