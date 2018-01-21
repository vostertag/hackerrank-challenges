#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    priceW = 0
    priceB = 0
    if(y > x+z):
        priceW = x+z
    else:
        priceW = y
    if(x > y+z):
        priceB = y+z
    else:
        priceB = x
    print(priceB*b+priceW*w)
        
    
    
    
