#!/usr/bin/python
'''
Design an algorithm and write code to remove the duplicate characters in a string without using any additional buffer.
NOTE: One or two addational variables are fine.
'''

import sys

def removeDupChar(str1):
    _lenStr1 = len(str1)
    if _lenStr1 == 0 or _lenStr1 == 1:
        return "there is no duplicate char in string"
    else:
        ch_list = [False]*256
        ch = ""
        for s in str1:
            _index = ord(s)-ord("a")
            if ch_list[_index]:
                pass
            else:
                ch_list[_index] = True
                ch += s
        return ch

if __name__ == "__main__":
    str1 = sys.argv[1]
    print removeDupChar(str1)
