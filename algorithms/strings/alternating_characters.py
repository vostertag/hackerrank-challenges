#!/bin/python3

import sys

def alternatingCharacters(s):
    newString = s[0]
    count = 0
    for i in range(1,len(s)):
        if(s[i-1] != s[i]):
            newString += s[i]
        else:
            count += 1
    return count

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = alternatingCharacters(s)
    print(result)
