#!/bin/python3

import sys

def fairRations(B):
    t = 0
    for i in range(len(B)):
        if(B[i]%2!=0):
            if(i<len(B)-1):
                B[i] += 1
                B[i+1] += 1
                t +=2
            else:
                return "NO"
    return t

if __name__ == "__main__":
    N = int(input().strip())
    B = list(map(int, input().strip().split(' ')))
    result = fairRations(B)
    print(result)
