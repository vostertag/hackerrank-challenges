#!/bin/python3

import sys
import math


n = int(input().strip())
a = []
sum1 = 0;
sum2 = 0;
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(len(a)):
    sum1 += a[i][i];
    sum2 += a[i][len(a) - 1 -i]
print(int(math.fabs(sum1-sum2)))
