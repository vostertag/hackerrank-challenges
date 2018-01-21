#!/bin/python3

import sys

def getRecord(s):
    max = s[0]
    min = s[0]
    nbTimeMax = 0
    nbTimeMin = 0
    for a in range(len(s)):
        if(s[a] > max):
            max = s[a]
            nbTimeMax += 1
        elif s[a]<min:
            nbTimeMin += 1
            min = s[a]
    return [nbTimeMax, nbTimeMin]

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
