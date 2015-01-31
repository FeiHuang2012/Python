#!/usr/bin/python
'''
Imagine a robot sitting on the upper left hand corner of an MxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
'''
import sys

def nPath(m, n):
    if (m == 1 or n == 1):
        return 1
    else:
        return nPath(m-1, n) + nPath(m, n-1)

if __name__ == "__main__":
    m = int(sys.argv[1])
    n = int(sys.argv[2])
    print nPath(m,n)
    

