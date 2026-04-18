from collections import deque, defaultdict

a, b = map(int, input().split())

dp = defaultdict(lambda: -1)
dp[a]=1
q = deque([a*2, a*10+1])

while len(q) > 0:
    i = q.popleft()
    if i > b:
        continue

    v = []

    if i % 2 == 0 and dp[i//2] != -1:
        v.append(dp[i//2]+1)

    if (i-1) % 10 == 0 and dp[(i-1)//10] != -1:
        v.append(dp[(i-1)//10]+1)

    if len(v) > 0:
        dp[i] = min(v)
        q.append(i*2)
        q.append(i*10+1)

    if i == b:
        break

print(dp[b])