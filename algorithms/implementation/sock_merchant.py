#!/bin/python3

import sys

def sockMerchant(n, ar):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if(ar[i] == ar[j] and ar[i] != None):
                pairs += 1
                ar[j] = None
                ar[i] = None
                break
    return pairs

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
