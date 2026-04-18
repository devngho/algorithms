from typing import Dict

N, M, V = map(int, input().split())
lines = set(tuple(sorted(map(int, input().split()))) for _ in range(M))
line_per_node: Dict[int, list] = {i: (sorted(list(set(map(lambda x: x[0] if x[0] != i else x[1], filter(lambda x: i in x, lines))))))
                                 for i in
                                 range(1, N + 1)}

visited = set()
result = []


def dfs(here=V):
    result.append(here)
    visited.add(here)
    for v in line_per_node[here]:
        if v not in visited:
            dfs(v)


def bfs(here=V):
    visited.add(here)
    q = [here]
    while len(q) > 0:
        v = q.pop(0)
        result.append(v)
        for i in line_per_node[v]:
            if i not in visited:
                visited.add(i)
                q.append(i)


dfs()
print(' '.join(map(str, result)))
result.clear()
visited.clear()
bfs()
print(' '.join(map(str, result)))
