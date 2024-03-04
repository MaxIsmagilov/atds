#!/usr/bin/env python3

"""
stack_comparison.py
Project description
"""

__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

import time
import random
from atds import Stack
from atds import UnorderedListStack

us = UnorderedListStack()
ls = Stack()

def get_times():
    t1 = 0
    t2 = 0
    value = random.randint(0, 2000)
    t1 = -time.time_ns()
    us.push(value)
    a = us.peek()
    a = us.pop()
    t1 += time.time_ns()
    t2 = -time.time_ns()
    ls.push(value)
    a = ls.peek()
    a = ls.pop()
    t2 += time.time_ns()
    
    us.push(0)
    ls.push(0)
    
    return [t1, t2]
        

def main():
    times = []
    for i in range (100000):
        us.push(i)
        ls.push(i)
        times.append(get_times())
    
    x_axs = [x for x in range(0, len(times))]
    us_times = [x[0] for x in times]
    ls_times = [x[1] for x in times]
    
    uavg = sum(us_times)/len(us_times)
    lavg = sum(ls_times)/len(ls_times)
    
    for i in range (0, 100000, 1000):
        print(f"Unordered at {i}: {us_times[i]} ns")
        print(f"List      at {i}: {ls_times[i]} ns")
    print("\n")
    print(f"Unordered : {uavg} ns")
    print(f"List      : {lavg} ns")
    print(f"The List is {((uavg/lavg) - 1)* 100}% faster")

if __name__ == "__main__":
    main()
