#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
while len(arr) > 0:
    print(len(arr))
    mini = min(arr)
    toDelete = []
    new_arr = []
    for i in range(len(arr)):
        arr[i] = arr[i] - mini
        if arr[i] != 0:
            new_arr.append(arr[i])
    arr = new_arr
    
            
    
