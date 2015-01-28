#!/usr/bin/python
'''
Write a method to decide if two strings are anagrams or not
ex:
  "abcca" "ccaba"
'''
import sys

def isAnagrams(str1, str2):
    _lenStr1 = len(str1)
    _lenStr2 = len(str2)
    if (_lenStr1 != _lenStr2):
        return "two strings are not anagrams"
    listStr1 = list(str1)
    listStr2 = list(str2)
    for i in listStr1:
        if i in listStr2:
            listStr2.remove(i)
        else:
            return False
    return True

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print isAnagrams(str1, str2)
