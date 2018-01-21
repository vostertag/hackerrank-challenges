#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    string = str(n)
    total = 0
    for i in string:
        if int(i) != 0 and n%int(i) == 0:
            total+=1
    print(total)
