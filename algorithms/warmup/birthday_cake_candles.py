#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    maxi = max(ar)
    count=0
    for i in range(len(ar)):
        if(ar[i] == maxi):
            count +=1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
