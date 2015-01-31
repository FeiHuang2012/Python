#!/usr/bin/python
'''
Write a method to generate the nth Fibonacci number
'''
import sys
#import pdb

def nthFibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        #pdb.set_trace()
        #print n
        return nthFibonacci(n-1) + nthFibonacci(n-2)

if __name__ == "__main__":
    n = int(sys.argv[1])
    print nthFibonacci(n)
