n, m = map(int, input().split())

arr=[list(map(int, input().split())) for _ in range(n)]
prefixes=[[arr[i][0]]*n for i in range(n)]

for i in range(n):
    for j in range(1, n):
        prefixes[i][j] = prefixes[i][j-1] + arr[i][j]

for _ in range(m):
    s=0
    y1, x1, y2, x2 = map(lambda x: int(x)-1, input().split())

    for i in range(y1, y2+1):
        s += prefixes[i][x2] - (prefixes[i][x1-1] if x1 != 0 else 0)

    print(s)