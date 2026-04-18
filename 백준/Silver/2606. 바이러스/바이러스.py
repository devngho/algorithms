from collections import deque

q = deque([1])
infected = [1]
n = int(input())
line_n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(line_n)]
nodes = {i+1: [] for i in range(n)}

for t in lines:
    a, b = t
    nodes[a].append(b)
    nodes[b].append(a)

while len(q) != 0:
    node = q.popleft()
    for i in nodes[node]:
        if i not in infected:
            q.append(i)
            infected.append(i)

print(len(infected)-1) # not 1