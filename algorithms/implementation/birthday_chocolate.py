#!/bin/python3

import sys

def solve(n, s, d, m):
    ways = 0
    for i in range(n):
        total = 0
        if(i+m <=n):
            for j in range(m):
                total += s[i+j]
            if total == d:
                ways += 1
    return ways
            

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
