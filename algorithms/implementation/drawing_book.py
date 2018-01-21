#!/bin/python3

import sys
import math

def solve(n, p):
    if(p<=(n/2)):
        return math.floor(p/2)
    else:
        if n%2==0:
            return math.ceil((n-p)/2)
        return math.floor((n-p)/2)

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
