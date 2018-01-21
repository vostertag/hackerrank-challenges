#!/bin/python3

import sys
import math


s = input().strip()
n = int(input().strip())
lettersLeft = n%len(s)
count = 0
countLeft = 0
for i in range(len(s)):
    if(s[i] == "a"):
        if(i < lettersLeft):
            countLeft += 1
        count +=1
print(count*math.floor(n/len(s))+countLeft)
