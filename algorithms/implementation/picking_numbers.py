#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
max = 0
a = sorted(a)
min = a[0]
count = 0
for i in a:
    if i > min+1:
        if count > max:
            max = count
        count = 1
        min = i
    else:
        count +=1 
if(count == len(a)):
    print(len(a))
else:
    print(max)
