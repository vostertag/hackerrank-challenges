import math

list = [int(s_temp) for s_temp in input().strip().split(' ')]
tot = 0
for i in range(list[0], list[1]+1):
    if(math.fabs(i - int(str(i)[::-1]))%list[2] == 0):
        tot += 1
print(tot)
