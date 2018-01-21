#!/bin/python3

import sys
import math

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
values = []
for i in range(n):
    for j in range(i+1, n):
        if(A[i] == A[j]):
            values.append(math.fabs(i-j))
if len(values) > 0: 
    print(int(min(values)))
else:
    print(-1)
            
