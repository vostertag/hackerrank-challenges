n = int(input().strip())
x = [int(a_temp) for a_temp in input().strip().split(' ')]
for i in range(1,n+1):
    print(x.index(x.index(i)+1)+1)
