#!/bin/python3

import sys

def saveThePrisoner(n, m, s):
    total = (s+m-1)%(n)
    if total == 0:
        return n
    else:
        return total

t = int(input().strip())
for a0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)
