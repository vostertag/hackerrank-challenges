#!/bin/python3

import sys


n = int(input().strip())

for i in range(n):
    for j in range(n-1-i):
        print(' ', end='')
    for j in range(i):
        print('#', end='')
    print('#')
