#!/bin/python3

import sys

def lonelyinteger(a):
    for i in range(len(a)):
        pair = False
        for j in range(len(a)):
            if j != i and a[j] == a[i]:
                pair=True
                break
        if not pair:
            return a[i]
    

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)
