#!/bin/python3

import sys


s = input().strip()
nbWords = 1
for i in s:
    if i.upper() == i:
        nbWords += 1
print(nbWords)
        
