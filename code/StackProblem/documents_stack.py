#!/usr/bin/env python3

"""
documents_stack.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "2024-02-15"

from atds import Stack

def time_to_int(timestring):
    pieces = timestring.split(':')
    mul = 3600
    f = 0
    for p in pieces:
        a = str(p).replace(':', '')
        f += int(a) * mul
        mul //= 60
    return f
    
def get_lines(filename):
    """
    imports all lines of a file
    """
    with open(filename, "r", encoding='utf-8') as fl:
        return fl.readlines()
    
def load_dropoff_log(filename):
    lst = get_lines(filename)
    newlst = [(l.split()) for l in lst]
    newerlst = [(time_to_int(l[1]), l[2]) for l in newlst]
    return newerlst

def load_pickup_log(filename):
    lst = get_lines(filename)
    newlst = [(l.split()) for l in lst]
    newerlst = [time_to_int(l[1]) for l in newlst]
    return newerlst

def run_prog(dropoffname, pickupname):
    s = Stack()
    d = load_dropoff_log(dropoffname)
    p = load_pickup_log(pickupname)
    # print(len(d)-len(p))
    for t in range(90000):
        for d_entry in d:
            if d_entry[0] == t:
                s.push(d)
                
        for p_entry in p:
            if p_entry == t:
                s.pop() # This will handle an empty case in case one exists
                
    # print(s.__repr__())  
    return s  

def main():
    s = run_prog("dropoff_log.txt", "pickup_log.txt")
    print(f"size of final stack: {s.size()}")
    print(f'       final number: "{(s.peek())[1][1]}"')

if __name__ == "__main__":
    main()
