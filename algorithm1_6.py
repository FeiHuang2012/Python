#!/usr/bin/python
'''
Given an image represented by an NxN matrix, write a method to rotate the image by 90 degrees
ex:
[1,2,3]        [3,6,9]
[4,5,6]   =>   [2,5,8]
[7,8,9]        [1,4,7]
'''

import sys
import json

def rotateNxNList(list1):
    _lenList1 = len(list1)
    #import pdb
    #pdb.set_trace()
    for i in range(_lenList1):
        for j in range(i):
            list1[i][j], list1[j][i] = list1[j][i], list1[i][j]
    for i in range(_lenList1/2):
        list1[i], list1[_lenList1-1-i] = list1[_lenList1-1-i], list1[i]
    print "The NxN list after rotate is:"
    for i in list1:
        print i
    return list1

if __name__ == "__main__":
    listarg = sys.argv[1]
    list1 = json.loads(listarg)
    rotateNxNList(list1) 
