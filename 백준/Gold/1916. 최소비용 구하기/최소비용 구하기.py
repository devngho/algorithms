import heapq
import sys

n,m=int(input()), int(input())
graph={k+1: {} for k in range(n)}

for _ in range(m):
    a, b, w = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(w, graph[a][b])
    else:
        graph[a][b] = w

a,b=map(int, input().split())

q=[(0, a)]
d=[sys.maxsize for _ in range(n)]

while len(q) > 0:
    v=heapq.heappop(q)

    for i in graph[v[1]]:
        if d[i-1] > v[0] + graph[v[1]][i]:
            d[i-1] = v[0] + graph[v[1]][i]
            heapq.heappush(q, (v[0]+graph[v[1]][i], i))

print(d[b-1])