import math

n = int(input().strip())
total = 0
newPeople = 5
for i in range(n):
    total += math.floor(newPeople/2)
    newPeople = math.floor(newPeople/2)*3
print(total)
