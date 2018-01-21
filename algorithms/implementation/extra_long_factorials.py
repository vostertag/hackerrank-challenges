#!/bin/python3

import sys


n = int(input().strip())
total=1
for i in range(n,1,-1):
    total *= i
print(total)
