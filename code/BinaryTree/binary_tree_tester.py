#!/usr/bin/env python3
"""
binary_tree_class_tester.py
This program tests the BinaryTree class.

To use this file, place it in the same directory as your binary_tree_class.py
file. Then run "python3 binary_tree_class_tester.py"

@author Richard White
@version 2018-04-12
"""

from atds import *

def main():
    print("Testing the binary_tree_class file!")
    bt = BinaryTree(3)
    print("Instruction: bt = BinaryTree(3)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=None,right_child=None]")
    print()
    bt.insert_left(4)
    print("Instruction: bt.insert_left(4)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    bt.insert_left(5)
    print("Instruction: bt.insert_left(5)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None]")
    print()
    bt.insert_right(6)
    print("Instruction: bt.insert_right(6)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=6,left_child=None,right_child=None]]")
    print()
    bt.insert_right(7)
    print("Instruction: bt.insert_right(7)")
    print("Result:", bt) 
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    l = bt.get_left_child()
    print("Instruction: l = bt.get_left_child()")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=5,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.set_root_val(9)
    print("Instruction: l.set_root_val(9)")
    print("Result: l =", l)
    print("Expect: l = BinaryTree[key=9,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None]")
    print()
    l.insert_left(11)
    print("Instruction: l.insert_left(11)")
    print("Result:", bt)
    print("Expect: BinaryTree[key=3,left_child=BinaryTree[key=9,left_child=BinaryTree[key=11,left_child=BinaryTree[key=4,left_child=None,right_child=None],right_child=None],right_child=None],right_child=BinaryTree[key=7,left_child=None,right_child=BinaryTree[key=6,left_child=None,right_child=None]]]")
    print()
    print("Instruction: print(bt.get_right_child().get_right_child())")
    print("Result:", bt.get_right_child().get_right_child())
    print("Expect: BinaryTree[key=6,left_child=None,right_child=None]")    


if __name__ == "__main__":
    main()