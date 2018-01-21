#!/bin/python3

import sys
import math


s = input().strip()
nbRows = round(math.sqrt(len(s)))
if(nbRows >= math.sqrt(len(s))):
    nbCol = nbRows
else:
    nbCol = nbRows+1
encrypt = []
for i in range(nbRows):
    encrypt.append([])
    for j in range(nbCol):
        if(i*nbCol + j < len(s)):
            encrypt[len(encrypt)-1].append(s[i*nbCol + j])
        else:
            encrypt[len(encrypt)-1].append("")
crypted = ""
for j in range(nbCol):
    for k in range(nbRows):
        crypted += encrypt[k][j]
    crypted += " "
print(crypted)
        
