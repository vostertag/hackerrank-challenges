#!/bin/python3

import sys

def strangeCode(t):
    total = 3
    lastMax = 6
    while total < t:
        total += lastMax
        lastMax *= 2
    return total-t+1
        
        
        

if __name__ == "__main__":
    t = int(input().strip())
    result = strangeCode(t)
    print(result)
