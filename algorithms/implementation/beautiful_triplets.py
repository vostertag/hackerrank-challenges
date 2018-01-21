n,d = input().strip().split(" ")
n,d = int(n), int(d)
triplet = list(map(int, input().strip().split(' ')))
total = 0
for i in range(len(triplet)):
    for j in range(i+1,len(triplet)):
        if(triplet[j] - triplet[i] == d):
            for k in range(j+1,len(triplet)):
                if triplet[k]-triplet[j] == d:
                    total +=1
                if(triplet[k]-triplet[j] > d):
                    break
        elif triplet[j] - triplet[i] > d:
            break
print(total)
