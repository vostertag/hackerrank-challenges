#!/bin/python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    alice = list(map(int, input().strip().split(' ')))
    scoresWithPos = []
    rank = 1
    best = scores[0]
    for i in scores:
        if(i < best):
            rank += 1
            best = i
        scoresWithPos.append([i, rank])
    scoresWithPos.append([alice[0], rank+1])
    scores.append(alice[0])
    pos = len(scoresWithPos)-1
    weAt=0
    for i in alice:
        j = pos
        while i >= scores[j] and j >= 0:
            j-=1
        pos = j+1
        print(scoresWithPos[pos][1])
        
        
        
        
            
            
            
