#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())
temp = t
while(s.find(temp,0) == -1):
    temp = temp[:-1]
minimum = len(s)-len(temp) + (len(t)-len(temp))
if minimum <= k and ((minimum-k)%2 == 0 or len(s)+len(t) <= k):
    print("Yes")
else:
    print("No")
