#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    for i in range(n):
        if i%2 == 0:
            height *=2
        else:
            height += 1
    print(height)
        
