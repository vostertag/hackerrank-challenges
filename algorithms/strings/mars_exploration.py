#!/bin/python3

import sys


s = input().strip()

sos = 'SOS'
count=0
pos = 0
for i in s:
    if(i != sos[pos]):
        count += 1
    pos += 1
    if(pos == 3):
        pos = 0
print(count)
