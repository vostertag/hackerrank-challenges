l = [int(s_temp) for s_temp in input().strip().split(' ')]
t1 = l[0]
t2 = l[1]
n = l[2]
for i in range(n-2):
    temp = t1 + t2*t2
    t1 = t2
    t2 = temp
print(temp)
