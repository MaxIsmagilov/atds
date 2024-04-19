#!/usr/bin/env python3

"""
binary_tree_traversal.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "2024-04-10"

from atds import BinaryTree

def preorder(t):
    return [] if t == None else [t.get_root_val()] + preorder(t.get_left_child()) + preorder(t.get_right_child()) 

def inorder(t):
    return [] if t == None else inorder(t.get_left_child())+ [t.get_root_val()] + inorder(t.get_right_child()) 

def postorder(t):
    return [] if t == None else postorder(t.get_left_child()) + postorder(t.get_right_child()) + [t.get_root_val()]    

def main():
    test_tree = BinaryTree('a', BinaryTree('b', BinaryTree('d', BinaryTree('h'), BinaryTree('i')), BinaryTree('e', right=BinaryTree('j'))), BinaryTree('c', BinaryTree('f'), BinaryTree('g', BinaryTree('k'))))
    print("preorder:", end='\t')
    print(preorder(test_tree))
    print("inorder:", end='\t')
    print(inorder(test_tree))
    print("postorder:", end='\t')
    print(postorder(test_tree))

if __name__ == "__main__":
    main()
