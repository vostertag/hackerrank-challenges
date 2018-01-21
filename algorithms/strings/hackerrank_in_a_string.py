#!/bin/python3

import sys


q = int(input().strip())
toFind = 'hackerrank'
for a0 in range(q):
    s = input().strip()
    found = True
    position = 0
    for i in toFind:
        position = s.find(i, position) + 1
        if(position == 0):
            found = False
            break
    if(found):
        print('YES')
    else:
        print('NO')
