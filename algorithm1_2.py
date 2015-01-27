#!/usr/bin/python
'''
reverse a sting
'''

import sys

def reverseStr(str1):
    _lenStr1 = len(str1)
    ch = ""
    if _lenStr1 == 0:
        return False
    elif _lenStr1 == 1:
        return str1
    else:
        while _lenStr1 > 0:
            ch += str1[_lenStr1-1]
            _lenStr1 -= 1
        return ch

if __name__ == "__main__":
    str1 = sys.argv[1]
    print reverseStr(str1)
