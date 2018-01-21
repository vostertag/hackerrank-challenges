#!/bin/python3

import sys
import math

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = input().strip().split(' ')
queen = [int(rQueen),int(cQueen)]
obstacles = []
for a0 in range(k):
    rObstacle,cObstacle = input().strip().split(' ')
    obstacles.append([int(rObstacle),int(cObstacle)])
toRemove = 0
toRemoveHere = 0
best = [0]*8

for i in obstacles:
    if i[0] == queen[0]:
        if(i[1] < queen[1]):
            toRemoveHere = i[1]
            if toRemoveHere > best[0]:
                toRemove += toRemoveHere - best[0]
                best[0] = toRemoveHere
        else:
            toRemoveHere = n+1-i[1]
            if toRemoveHere > best[1]:
                toRemove += toRemoveHere - best[1]
                best[1] = toRemoveHere
    elif i[1] == queen[1]:
        if(i[0] < queen[0]):
            toRemoveHere = i[0]
            if toRemoveHere > best[2]:
                toRemove += toRemoveHere - best[2]
                best[2] = toRemoveHere
        else:
            toRemoveHere = n+1-i[0]
            if toRemoveHere > best[3]:
                toRemove += toRemoveHere - best[3]
                best[3] = toRemoveHere
    elif math.fabs(queen[0] - i[0]) == math.fabs(queen[1] - i[1]):
        if(i[1] < queen[1]):
            if(i[0] < queen[0]):
                toRemoveHere = min([i[0]-1, i[1]-1]) + 1
                if toRemoveHere > best[4]:
                    toRemove += toRemoveHere - best[4]
                    best[4] = toRemoveHere
            else:
                toRemoveHere = min([n-i[0],i[1]-1]) + 1
                if toRemoveHere > best[5]:
                    toRemove += toRemoveHere - best[5]
                    best[5] = toRemoveHere
        else:
            if(i[0] < queen[0]):
                toRemoveHere = min([n-i[1], i[0]-1]) + 1
                if toRemoveHere > best[6]:
                    toRemove += toRemoveHere - best[6]
                    best[6] = toRemoveHere
            else:
                toRemoveHere = min([n-i[0],n-i[1]]) + 1
                if toRemoveHere > best[7]:
                    toRemove += toRemoveHere - best[7]
                    best[7] = toRemoveHere
allAttacks = (n-1)*2 + min([queen[0]-1, queen[1]-1]) + min([n-queen[1], queen[0]-1]) + min([n-queen[0],queen[1]-1]) + min([n-queen[0],n-queen[1]])
print(allAttacks-toRemove)
        
