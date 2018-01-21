import math

n = int(input().strip())
for i in range(n):
    a,b = input().strip().split(" ")
    a,b = int(a), int(b)
    print(int(math.floor(math.sqrt(b))-math.ceil(math.sqrt(a)))+1)
