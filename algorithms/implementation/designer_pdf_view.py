#!/bin/python3

import sys
import string

h = list(map(int, input().strip().split(' ')))
word = input().strip()

max = 0
for i in word:
    if(h[string.ascii_lowercase.index(i)] > max):
        max = h[string.ascii_lowercase.index(i)]
print(max*len(word))
