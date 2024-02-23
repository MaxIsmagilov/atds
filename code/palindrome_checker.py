#!/usr/bin/env python3

"""
palindrome_checker.py
Checks if something is a palindrome
"""
__author__ = "Max Ismagilov"
__version__ = "2024-02-22"

from atds import Deque



class PalindromeChecker:
    
    def __init__(self, set_strict=False) -> None:
        self.do_strict = set_strict
        
    def set_strict_mode(self, is_on):
        """ 
        sets strict mode on or off. strict mode means that the string is 
        interpereted exactly. Non-strict mode only considers letters; capitalization does not matter. Defaults to True.
        """
        self.do_strict = is_on
    
    def sanitize_string(string):
        """Sanitizes a string; this function will strip all non-letter characters and set all letters to lowercase"""
        return ''.join([(x.lower() if x.lower() in list("abcdefghijknmnopqrstuvwxyz") else '') for x in string])
        
    def is_palindrome(self, string):
        """Finds if a string is a palindrome

        Args:
            string (str): The string in question

        Returns:
            bool: whether the string is a palindrome or not
        """
        test_string = string if self.do_strict else PalindromeChecker.sanitize_string(string)
        forwards_d  = Deque()
        backward_d  = Deque()  
        
        for char in test_string:
            forwards_d.add_front(char)
            backward_d.add_rear (char)
            
        while (not (forwards_d.is_empty() or backward_d.is_empty())):
            if forwards_d.remove_front() != backward_d.remove_front():
                return False
            else:
                pass
        return True
            

def sus_check_palindrome(string, do_strict=False):
    test_string = string if do_strict else PalindromeChecker.sanitize_string(string)
    d = Deque()
    for char in range(len(test_string)//2):
        d.add_front(test_string[char])
    for char in range(len(test_string)//2 + (len(test_string) % 2), len(test_string)):
        if (d.remove_front() != test_string[char]):
            return False
    return True

def main():
    pass

if __name__ == "__main__":
    main()
