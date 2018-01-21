#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
nbZer, nbPos, nbNeg = 0, 0, 0
for i in range(len(arr)):
    if(arr[i] > 0):
        nbPos += 1
    elif arr[i]<0:
        nbNeg += 1
    else:
        nbZer += 1

print(nbPos/n)
print(nbNeg/n)
print(nbZer/n)
