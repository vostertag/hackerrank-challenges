#!/bin/python3

import sys
import math

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    lenA = math.fabs(z-x)
    lenB = math.fabs(z-y)
    if(lenA < lenB):
        print('Cat A')
    elif(lenA > lenB):
        print('Cat B')
    else:
        print('Mouse C')
