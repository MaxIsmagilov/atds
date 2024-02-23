#!/usr/bin/env python3

"""
paren_checker.py
checks legality of parentheses
"""
__author__ = "Max Ismagilov"
__version__ = "2024-02-13"

from atds import Stack

def is_valid(expr):
    s = Stack()
    for t in list(expr):
        if t == '(' or t == ')':
            s.push(t)
    i = 0
    while (not s.is_empty()):
        i += 1 if s.peek() == "(" else -1
        if (i > 0):
            return False
        s.pop()
    return i == 0
    

def main():
    pass

if __name__ == "__main__":
    main()
