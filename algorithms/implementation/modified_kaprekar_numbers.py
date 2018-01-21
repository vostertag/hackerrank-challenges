#!/bin/python3

import sys
import math

def kaprekarNumbers(p, q):
    one = False
    for i in range(p,q+1):
        number = i*i
        string = str(number)
        n1,n2 = "",""
        if(number/10 >= 1):
            for j in range(math.floor(len(string)/2)):
                n1+=string[j]
                n2+=string[len(string)-1-j]
            if(len(string)%2 == 1):
                n2 += string[math.floor(len(string)/2)]
            n2 = n2[::-1] 
            if(int(n2) + int(n1) == i):
                print(i, end=" ")
                one = True
        else:
            if(i*i == i):
                print(i, end=" ")
                one = True
    if not one:
        print("INVALID RANGE")

if __name__ == "__main__":
    p = int(input().strip())
    q = int(input().strip())
    result = kaprekarNumbers(p, q)
    print (" ".join(map(str, result)))


