from collections import deque

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    arr = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[x][y] = 1

    blocks = 0

    def bfs(init_x, init_y):
        q = deque([(init_x, init_y)])

        while len(q) != 0:
            x, y = q.popleft()
            if not (0 <= x < m and 0 <= y < n): continue

            if arr[x][y] == 1:
                arr[x][y] = 0
                q.append((x-1, y))
                q.append((x+1, y))
                q.append((x, y-1))
                q.append((x, y+1))

    for x in range(m):
        for y in range(n):
            if arr[x][y] == 1:
                bfs(x, y)
                blocks += 1
    print(blocks)