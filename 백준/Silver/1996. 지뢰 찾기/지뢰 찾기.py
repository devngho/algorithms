s=int(input())
arr=[[0]*s for _ in range(s)]

for y in range(s):
    inp=input()
    for x in range(s):
        if inp[x] == '.':
            arr[y][x]=0
        else:
            arr[y][x]=int(inp[x])

res=[['0']*s for _ in range(s)]

for y in range(s):
    for x in range(s):
        if arr[y][x] != 0:
            res[y][x]='*'
            continue
        
        total=0
        for j in range(max(0, y-1), min(s, y+2)):
            for i in range(max(0, x-1), min(s, x+2)):
                total+=arr[j][i]
        
        if total >= 10:
            res[y][x]='M'
        else:
            res[y][x]=str(total)
print('\n'.join(map(lambda x: ''.join(x), res)))