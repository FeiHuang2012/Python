#!/usr/bin/python
'''
Wirte code to remove duplicates from an unsorted list, how would you solve this problem if a temporary buffer is not allowed
'''
import sys
import json

def removeDupinList(list1):
    _lenList1 = len(list1)
    if _lenList1 < 2:
        return list1
    i = 0
    while i < _lenList1:
        j = i + 1
        while j < _lenList1:
            if list1[i] == list1[j]:
                del(list1[j])
                _lenList1 -= 1
            j += 1
        i += 1
    return list1

if __name__ == "__main__":
    strlist1 = sys.argv[1]
    list1 = json.loads(strlist1)
    print removeDupinList(list1)       
                
