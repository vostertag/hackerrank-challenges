n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
freq = {}
for i in ar:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(n - max(freq.values()))
