#!/bin/python3

import sys

def gridSearch(G, P):
    for i in range(len(G)):
        start = -1
        goOn = True
        while(goOn):
            line = 0
            start = G[i].find(P[line], start+1)
            if(start == -1):
                goOn = False
                break
            if i+len(P)-1 < len(G) and start != -1:
                line = 1
                for j in range(i+1, i+len(P)):
                    if G[j].find(P[line], start, start+len(P[0])) == -1:
                        break
                    else:
                        line += 1
                if(line == len(P)):
                    return "YES"
    return "NO"
    
    
    
    numberOfLines = 0
    for line in G:
        if P[numberOfLines] in line:
            numberOfLines += 1
            if(numberOfLines == len(P)-1):
                return "YES"
        else:
            numberOfLines = 0
    return "NO"
        
        
        
            

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        R, C = input().strip().split(' ')
        R, C = [int(R), int(C)]
        G = []
        G_i = 0
        for G_i in range(R):
           G_t = str(input().strip())
           G.append(G_t)
        r, c = input().strip().split(' ')
        r, c = [int(r), int(c)]
        P = []
        P_i = 0
        for P_i in range(r):
           P_t = str(input().strip())
           P.append(P_t)
        result = gridSearch(G, P)
        print(result)
