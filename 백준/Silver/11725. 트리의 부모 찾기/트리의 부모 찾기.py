import sys
sys.setrecursionlimit(110000)

n = int(input())
graph = {k: [] for k in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parents = {k: -1 for k in range(1, n+1)}
parents[1] = -1

def dfs(node):
    for i in graph[node]:
        if parents[i] == -1:
            parents[i] = node
            dfs(i)

dfs(1)

for i in range(2, n+1):
    print(parents[i])