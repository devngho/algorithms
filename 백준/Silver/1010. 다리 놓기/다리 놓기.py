dp=[[-1] * 31 for _ in range(31)]

def count(n, m):
    if dp[n][m] != -1:
        pass
    elif n == m:
        dp[n][m] = 1
    elif n > m:
        dp[n][m] = 0
    elif n == 1:
        dp[n][m] = m
    else:
        dp[n][m] = sum([count(n-1, m-i) for i in range(1, m-n+2)])
        
    return dp[n][m]

for _ in range(int(input())):
    n,m=map(int,input().split())

    print(count(n,m))