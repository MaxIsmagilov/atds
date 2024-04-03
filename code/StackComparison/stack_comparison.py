#!/usr/bin/env python3

"""
stack_comparison.py
Project description
"""

__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

import time
from atds import Stack
from atds import UnorderedListStack
import matplotlib.pyplot as plt

us = UnorderedListStack()
ls = Stack()

def get_times(push_count):
    t1 = 0
    t2 = 0
    t1 = -time.time_ns()
    for i in range(push_count):
        us.push(i)
    t1 += time.time_ns()
    t2 = -time.time_ns()
    for i in range(push_count):
        ls.push(i)
    t2 += time.time_ns()
    
    return t1, t2
         
def plot (x, a, b):
    ax = plt.subplot()
    ax.plot(x, b, 'go', label="Unordered List Stack")
    ax.plot(x, a, 'b+', label="Python List Stack")
    ax.set_xlabel("Number of items in list")
    ax.set_ylabel("nanoseconds to push n numbers")
    ax.set_title("Time taken to push n values vs. Number of items contained\n in Stacks for Unordered List and Python List")
    highest = sorted(a + b, reverse=True)[20]
    ax.set_ylim(bottom=0, top=highest*1.1)
    ax.legend()
    plt.show()
    plt.savefig("stack_comparison.png")
    

def main():
    times = []
    for i in range (1_000):
        times.append(get_times(i))
    
    x_axs = [x for x in range(0, len(times))]
    us_times = [x[0] for x in times]
    ls_times = [x[1] for x in times]
    
    uavg = sum(us_times)/len(us_times)
    lavg = sum(ls_times)/len(ls_times)
    
    print("\n")
    print(f"Unordered : {uavg} ns")
    print(f"List      : {lavg} ns")
    print(f"The List is {((uavg/lavg) - 1)* 100}% faster")
    
    plot(x_axs, ls_times, us_times)

if __name__ == "__main__":
    main()
