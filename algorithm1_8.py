#!/usr/bin/python
'''
Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring 
ex:
 ''waterbottle" is a rotation of "erbottlewat".
'''
import sys

def isRotationString(str1, str2):
    if len(str1) != len(str2):
        return False
    _lenStr1 = len(str1)
    for i in range(_lenStr1):
        for j in range(_lenStr1):
            if(str1[i] == str2[j]):
                while i < _lenStr1:
                    if(str1[i] == str2[j]):
                        i += 1
                        j += 1
                        if j == _lenStr1:
                            j = 0
                    else:
                        return False
                return True
            else:
                pass
    return False

if __name__ == "__main__":
    str1 = sys.argv[1]
    str2 = sys.argv[2]
    print isRotationString(str1, str2)            

