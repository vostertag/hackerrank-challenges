#!/bin/python3

import sys
import math

def flatlandSpaceStations(n, c):
    c.sort()
    max = 0
    for a in range(len(c)-1):
        if(math.floor((c[a+1] - c[a])/2) > max):
            max = math.floor((c[a+1] - c[a])/2)  
    if(c[0] > max):
        max = c[0]
    if n-c[len(c)-1]-1>max:
        max = n-c[len(c)-1]-1
    return max
        
            

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatlandSpaceStations(n, c)
    print(result)
