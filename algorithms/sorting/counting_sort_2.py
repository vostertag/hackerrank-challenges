n = int(input().strip())
l = list(map(int, input().strip().split(' ')))
l = sorted(l)
for i in l:
    print(i, end=' ')
