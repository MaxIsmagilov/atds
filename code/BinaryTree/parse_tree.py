#!/usr/bin/env python3

"""
parse_tree.py
Project description
"""
__author__ = "Max Ismagilov"
__version__ = "YYYY-MM-DD"

from atds import BinaryTree

def build_parse_tree(expr):
    if len(expr) == 1:
        return BinaryTree(expr[0])
    if type(expr) == str:
        expr = expr.split()
    # print("DEBUG: ", expr)
    expr = expr[1:len(expr)-1]
    opnd1 = None
    opnd2 = None
    oprtr = None
    pcount = 0
    last = 0
    for i in range(len(expr)):
        if expr[i] == '(':
            pcount += 1
            continue
        if expr[i] == ')':
            pcount -= 1
        if pcount == 0:
            if opnd1 == None:
                opnd1 = expr[last:i+1]
                last = i+1
            elif oprtr == None:
                oprtr = expr[last]
                last = i+1
            else:
                opnd2 = expr[last:]
    return BinaryTree(oprtr, build_parse_tree(opnd1), build_parse_tree(opnd2))
            
    
def evaluate(parse_tree):
    if (parse_tree.get_left_child() == None or parse_tree.get_right_child() == None):
        if (parse_tree.get_left_child() != parse_tree.get_right_child()):
            raise Exception(f"The parse tree {parse_tree}\nis not well formed")
        return float(parse_tree.get_root_val())
    opnd1 = evaluate(parse_tree.get_left_child())
    opnd2 = evaluate(parse_tree.get_right_child())
    sign = parse_tree.get_root_val()
    match sign:
        case "**":
            return opnd1 ** opnd2
        case "*":
            return opnd1 * opnd2
        case "/":
            return opnd1 / opnd2
        case "+":
            return opnd1 + opnd2
        case "-":
            return opnd1 - opnd2   
    raise ArithmeticError(f"operator {sign} is invalid")             
    


def main():
    EPSILON = 0.001     # Used to accept results of limited precision
    tests = [("( 2 + 3 )", 5),
             ("( 1 / 3 )", 1/3),
             ("( ( 3 + 5 ) * 2 )", 16),
             ("( 3 + ( 5 * 2 ) )", 13),
             ("( ( 2 + ( 6 * 7 ) ) - 1 )", 43),
             ("( ( ( ( 4 / 1 ) - ( 4 / 3 ) ) + ( 4 / 5 ) ) - ( 4 / 7 ) )", 3.1416)]

    '''
    Add these tests later on once the first test is working:
             ("( 1 / 3 )", 1/3),
             ("( ( 3 + 5 ) * 2 )", 16),
             ("( 3 + ( 5 * 2 ) )", 13),
             ("( ( 2 + ( 6 * 7 ) ) - 1 )", 43),
             ("( ( ( ( 4 / 1 ) - ( 4 / 3 ) ) + ( 4 / 5 ) ) - ( 4 / 7 ) )", 3.1416)]
    '''

    for i in range(len(tests)):
        # Build the parse tree based on fully-parenthesized 
        # expression
        print("Testing expression",tests[i][0])
        pt = build_parse_tree(tests[i][0])
        # print("DEBUG:", (pt))
        # Now evaluate the expression, recursively!
        # result = evaluate(pt)
        # print("DEBUG:",result)
        print("Result:",evaluate(pt))
        if abs(evaluate(pt) - tests[i][1]) < EPSILON:
            print("Test",i + 1,"passed")
        else:
            print("Test",i + 1,"failed")
    print("""Test 6 should fail. It's an attempt to calculate pi that doesn't 
get very far.""")


if __name__ == "__main__":
    main()
