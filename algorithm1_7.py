#!/usr/bin/python
'''
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0
ex:
[1,2,3,4]     [1,0,3,4] 
[4,0,6,5]  => [0,0,0,0]
[7,8.9,6]     [7,0,9,6]
'''
import sys
import json

def setMatrixValue(list1):
    printList(list1)
    _lenlist1i = len(list1)
    for i in range(_lenlist1i):
        _lenlist1j = len(list1[i])
        for j in range(_lenlist1j):
            if list1[i][j] == 0:
                for k in range(_lenlist1i):
                    if k == i:
                        pass 
                    elif list1[k][j] == 0:
                        pass
                    else:
                        list1[k][j] = True
                for l in range(_lenlist1j):
                    if l == j:
                        pass
                    elif list1[i][l] == 0:
                        pass
                    else:
                        list1[i][l] = True
    for i in range(_lenlist1i):
        _lenlist1j = len(list1[i])
        for j in range(_lenlist1j):
            if list1[i][j] == True:
                list1[i][j] = 0
    printList(list1)
    return list1

def printList(list1):
    for i in list1:
        print i

if __name__ == "__main__":
    listarg1 = sys.argv[1]
    list1 = json.loads(listarg1)
    setMatrixValue(list1)
