#!/bin/python3

import sys

def migratoryBirds(n, ar):
    number = [0,0,0,0,0]
    for i in range(n):
        number[ar[i]-1] += 1
        
    return number.index(max(number))+1
            

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
