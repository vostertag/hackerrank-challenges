#!/bin/python3

import sys
import math

def theLoveLetterMystery(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cost = 0
    for i in range(math.floor(len(s)/2)):
        if(s[i] != s[len(s)-1-i]):
            cost += math.fabs(alphabet.find(s[i]) - alphabet.find(s[len(s)-1-i]))
    return int(cost)
            
    

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)
