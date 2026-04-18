from collections import deque

n, k = map(int, input().split())

if n == k:
    print(0)
else:
    visited = [100000] * 100001
    pos = deque([(0, n)])

    while True:
        i = pos.popleft()

        if i[1] == k:
            print(i[0])
            break

        n = i[1]+1
        if (0 <= n <= 100000) and visited[n] > i[0]:
            pos.append((i[0]+1, n))
            visited[n] = i[0] + 1

        n = i[1] - 1
        if (0 <= n <= 100000) and visited[n] > i[0]:
            pos.append((i[0]+1, n))
            visited[n] = i[0] + 1

        n = i[1] * 2
        if (0 <= n <= 100000) and visited[n] > i[0]:
            pos.appendleft((i[0], n))
            visited[n] = i[0]