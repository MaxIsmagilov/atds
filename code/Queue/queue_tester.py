#!/usr/bin/env python3
"""
queue_tester.py
Demonstrates the use of the Queue class.
@author Richard White
@version 2016-12-17
"""
from atds import Queue
def main():
    print("Testing the Queue class")
    testsPassed = 0
    try:
        q = Queue()
        print("Test passed: queue created")
        testsPassed += 1
    except:
        print("Test failed: couldn't initialize queue")
    try:
        q.enqueue("hello")
        q.enqueue(3)
        testsPassed += 1
        print("Test passed: items queued")
    except:
        print("Test failed: couldn't push onto queue")
    try:
        result = q.dequeue()
        if (result == "hello"):
            testsPassed += 1
            print("Test passed: item dequeued")
        else:
            print("Test failed: incorrect dequeue result")
    except:
        print("Test failed: couldn't dequeue")
    try:
        result = q.is_empty()
        if (not result):
            testsPassed += 1
            print("Test passed: is_empty returned correct result")
        else:
            print("Test failed: queue has items, but indicated empty")
    except:
        print("Test failed: is_empty() method unavailable")
    try:   
        result = q.size()
        if (result == 1):
            testsPassed += 1
            print("Test passed: correct size returned")
        else:
            print("Test failed: incorrect size returned")
    except:
        print("Test failed: .size() method unavailable")
    try:
        q.dequeue()
    except:
        pass
    try:
        result = q.is_empty()
        if (result):
            testsPassed += 1
            print("Test passed: is_empty() correctly indicating empty status")
        else:
            print("Test failed: queue failed to indicate empty status")
    except:
        print("Test failed: is_empty() unavailable")
        print(str(testsPassed) + "/6 tests passed")
        
if __name__ == "__main__":
    main()