#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
max = max(height)
if(k>max):
    print(0)
else:
    print(max-k)
