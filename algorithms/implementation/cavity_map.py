#!/bin/python3

import sys

def cavityMap(grid):
    if(len(grid[0]) > 1):
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                if(grid[i][j+1] != "X" and grid[i][j-1] != "X" and grid[i+1][j] != "X" and grid[i-1][j] != "X"):
                    if int(grid[i][j]) > int(grid[i][j+1]) and int(grid[i][j]) > int(grid[i][j-1]) and int(grid[i][j]) > int(grid[i-1][j]) and int(grid[i][j]) > int(grid[i+1][j]):
                        s = list(grid[i])
                        s[j] = "X"
                        grid[i] = "".join(s)
            
    return grid
        
            
            

if __name__ == "__main__":
    n = int(input().strip())
    grid = []
    grid_i = 0
    for grid_i in range(n):
       grid_t = str(input().strip())
       grid.append(grid_t)
    result = cavityMap(grid)
    print ("\n".join(map(str, result)))


