n=int(input())
dp=[False]*max(n, 4)
dp[1]=True
dp[3]=True
for i in range(4,n):
    dp[i]=not dp[i-4] or not dp[i-1] or not dp[i-3]
print('SK' if dp[n-1] else 'CY')