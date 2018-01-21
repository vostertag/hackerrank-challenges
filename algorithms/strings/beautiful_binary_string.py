#!/bin/python3

import sys

def minSteps(n, B):
    return B.count("010")

n = int(input().strip())
B = input().strip()
result = minSteps(n, B)
print(result)
