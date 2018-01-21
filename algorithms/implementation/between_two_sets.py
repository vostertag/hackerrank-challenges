#!/bin/python3

import sys

def getTotalX(a, b):
    between = 0
    maxi = min(b)
    x = 1
    total = 0
    while x<=maxi:
        work = True
        for ai in a:
            if(x%ai != 0):
                work = False
        if work:
            for bi in b:
                if(bi%x!=0):
                    work = False
            if work:
                total += 1
        x += 1
    return total
    
    

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
