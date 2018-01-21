#!/bin/python3

import sys

def timeConversion(s):
    format = s[-2:]
    s = s.replace(s[-2:], '')
    beginning = s[:2]
    s = s.replace(s[:2], '')
    beginning2 = int(beginning)
    if(format == 'PM'):
        if(beginning2 < 12):
            beginning2 += 12
            beginning = str(beginning2)
        return str(beginning) + s
    else:
        if beginning2 == 12:
            beginning = '00'
        return beginning + s;

s = input().strip()
result = timeConversion(s)
print(result)
