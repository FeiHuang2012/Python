#!/usr/bin/python
'''
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
'''
import sys

def isUnique2(str1):
    _lenStr1 = len(str1)
    setStr1 = set(str1)
    _lenSetStr1 = len(setStr1)
    if _lenStr1 == _lenSetStr1:
        return True
    else:
        return False 

if __name__ == "__main__":
    str1 = sys.argv[1]
    print isUnique2(str1)
