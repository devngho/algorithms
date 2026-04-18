s,k=input(),int(input())
groups=[]
for i in s:
    if i == ':':
        continue
    
    if len(groups) == 0 or groups[-1][0] != i:
        groups.append([i, 1])
    else:
        groups[-1][1] += 1

print(sum(map(lambda x: 2 if x[1]==1 else 2+len(str(x[1])), groups)))