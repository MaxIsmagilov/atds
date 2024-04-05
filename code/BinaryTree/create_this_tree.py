#!/usr/bin/env/ python3
"""
create_this_tree.py
Write a main program to create each of the trees given here.
This program prints out expected results based on a __str__() or __repr__() method 
being availabe for the BinaryTree class.
"""

from atds import BinaryTree

def main():
    print('''
    bt1:
                           A
                         /   \\
                        B     C
                      /
                     D
        ''')
    print('''Expected result, bt1:
    BinaryTree[key=A,left_child=BinaryTree[key=B,left_child=BinaryTree[key=D,left_child=None,right_child=None],right_child=None],right_child=BinaryTree[key=C,left_child=None,right_child=None]]''')
    print('--------------------')
    print("Example Solution")
    print('My result:')
    bt1 = BinaryTree('A')
    bt1.insert_right('C')
    bt1.insert_left('D')
    bt1.insert_left('B')
    print(bt1)
    print('--------------------')
    # Another way of doing the same tree
    bt1a = BinaryTree('A')
    bt1a.insert_left('B')
    bt1a.get_left_child().insert_left('D')
    bt1a.insert_right('C')
    print(bt1a)
    print('--------------------')
    print('''
    bt2:
                            A
                          /   \\
                         /     \\
                        B       C
                         \\     / \\
                          D   E   F
    ''')
    print('''Expected result bt2:
    BinaryTree[key=A,left_child=BinaryTree[key=B,left_child=None,right_child=BinaryTree[key=D,left_child=None,right_child=None]],right_child=BinaryTree[key=C,left_child=BinaryTree[key=E,left_child=None,right_child=None],right_child=BinaryTree[key=F,left_child=None,right_child=None]]]''')
    print('--------------------')
    print('My result:')

    boy = BinaryTree('A')
    boy.insert_left('B')
    boy.get_left_child().insert_right('D')
    boy.insert_right('F')
    boy.insert_right('C')
    boy.get_right_child().insert_left('E')
    print('    ',end='')
    print(boy)

    print('--------------------')
    print('''
    bt3:
                            A
                              \\
                                B
                               / 
                             C
                            / \\ 
                          D    E
    ''')

    print('''Expected result bt3:
    BinaryTree[key=A,left_child=None,right_child=BinaryTree[key=B,left_child=BinaryTree[key=C,left_child=BinaryTree[key=D,left_child=None,right_child=None],right_child=BinaryTree[key=E,left_child=None,right_child=None]],right_child=None]]''')
    print('--------------------')
    print('My result:')

    boy = BinaryTree('A', right=BinaryTree('B', BinaryTree('C', BinaryTree('D'), BinaryTree('E'))))    
    print('    ',end='')
    print(boy)

    print('--------------------')
    print('''
    bt4:
                            A
                          /   \\
                        /       \\
                      /           \\
                    B               C
                  /   \\           /   \\
                /       \\       /       \\
              D           E   F           G
            /   \\       /
           H      I    J
    ''')

    print('''Expected result bt4:
    BinaryTree[key=A,left_child=BinaryTree[key=B,left_child=BinaryTree[key=D,left_child=BinaryTree[key=H,left_child=None,right_child=None],right_child=BinaryTree[key=I,left_child=None,right_child=None]],right_child=BinaryTree[key=E,left_child=BinaryTree[key=J,left_child=None,right_child=None],right_child=None]],right_child=BinaryTree[key=C,left_child=BinaryTree[key=F,left_child=None,right_child=None],right_child=BinaryTree[key=G,left_child=None,right_child=None]]]''')
    print('--------------------')
    print('My result:')
    
    boy = BinaryTree('A', BinaryTree('B', BinaryTree('D', BinaryTree('H'),BinaryTree('I')),\
        BinaryTree('E', BinaryTree('J'))),BinaryTree('C', BinaryTree('F'), BinaryTree('G')))    
    print('    ',end='')
    print(boy)
    
    print('--------------------')
    


main()