#!/usr/bin/python
'''
Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?
'''
import sys

def isUnique(str1):
    ch = [0]*2555556
    for s in str1:
        _index = ord(s) - ord('a')
        if ch[_index] == 1:
            return False
        else:
            ch[_index] = 1
    return True

if __name__ == "__main__":
    str1 = sys.argv[1]
    print isUnique(str1)
