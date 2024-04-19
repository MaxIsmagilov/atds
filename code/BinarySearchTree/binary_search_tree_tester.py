#!/usr/bin/env python3

"""
binary_search_tree_tester.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

from atds import BinarySearchTree

def main():
    print("Testing BinarySearchTree class")
    bst = BinarySearchTree()
    bst.put(4,"Hi")
    bst.put(6,"Hi")
    bst.put(2,"Hi")
    bst.put(1,"Hi")
    bst.put(5,"Hi")
    bst.put(7,"Hi")
    bst.put(3,"Hi")
    for el in bst:
        print(el)
    print("Trying to replace key 6...")
    bst.put(6,"Hey!")
    for el in bst:
        print(el)    

if __name__ == "__main__":
    main()
