n = input().strip();
moves = input().strip();
weAt = 0
total = 0
valleyStart = False
for i in moves:
    if i == 'U':
        weAt += 1
    else:
        weAt -= 1
    if weAt < 0 and not valleyStart:
        valleyStart = True
    if weAt >= 0 and valleyStart:
        valleyStart = False
        total +=1
print(total)
