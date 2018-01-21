#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    due = sum(ar[i]/2 for i in range(len(ar)) if i != k)
    if due == b:
        return 'Bon Appetit'
    else:
        return int(b-due)
        

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
