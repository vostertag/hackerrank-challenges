#!/bin/python3

import sys
import math


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    choc = math.floor(n/c)
    temp = choc
    while(temp >= m):
        choc += math.floor(temp / m)
        temp = math.floor(temp/m) + temp%m
    print(choc)
