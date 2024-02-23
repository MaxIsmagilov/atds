#!/usr/bin/env python3

"""
hot_potato.py
Is hot potato
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

from atds import Queue
import random

STARTING_LIST = ['John Cena', 'Dwayne "The Rock" Johnson', 'Matthew Bristing', 'Xi Jinping', 'Jill Biden', '1993 Maynard James Keenan']

def play_until_dropped(queue):
    q = queue
    print(q.__repr__())
    while (True):
        mv = q.dequeue()
        if (random.randint(0, 10) == 0):
            print(f"{mv} dropped the potato!\n")
            return q
        else:
            print(f"{mv} passed on the potato!")
            q.enqueue(mv)
        
        
        

def main():
    q = Queue()
    for e in STARTING_LIST:
        q.enqueue(e)
    while (q.size() > 1):
        q = play_until_dropped(q)
    print(f"\n{q.peek()} Has Won!!!")

if __name__ == "__main__":
    main()
