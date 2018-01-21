#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
values = []
for topic_i in range(n):
    topic_t = str(input().strip())
    for top in topic:
        teamValue = str(int(top) + int(topic_t))
        nbTopics = teamValue.count("1") + teamValue.count("2")
        values.append(nbTopics)
    topic.append(topic_t)
maxi = max(values)
nbTeam = 0
for i in values:
    if i == maxi:
        nbTeam += 1
print(maxi)
print(nbTeam)
        
    
