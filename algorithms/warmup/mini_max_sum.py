#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
sorted(arr);
sum = sum(arr)
print(str(sum-max(arr)) + ' ' + str(sum-min(arr)))
