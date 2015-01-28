#!/usr/bin/python
'''
Write a method to replace all spaces in a string with '%20'
'''
import sys

def replaceStr(str1, ch1, ch2):
    if ch1 not in str1:
        return false
    listStr1 = list(str1)
    _lenListStr1 = len(listStr1)
    for i in range(_lenListStr1):
        if listStr1[i] == ch1:
            listStr1[i] = ch2
    str1List = ''.join(listStr1)
    return str1List

if __name__ == "__main__":
    str1 = sys.argv[1]
    ch1 = sys.argv[2]
    ch2 = sys.argv[3]
    print replaceStr(str1, ch1, ch2)
            
