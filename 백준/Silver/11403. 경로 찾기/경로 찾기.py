from collections import deque

n=int(input())
arr=[['0']*n for _ in range(n)]
graph=[list(map(lambda x: x[0], filter(lambda x: x[1] == '1', enumerate(input().split())))) for _ in range(n)]

for i in range(n):
    q=deque(graph[i])
    while len(q) > 0:
        v=q.popleft()
        if arr[i][v] != '1':
            arr[i][v] = '1'
            for j in graph[v]:
                q.append(j)

print(*map(lambda x: ' '.join(x),arr),sep='\n')