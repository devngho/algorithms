import math
from collections import defaultdict

n = int(input())

if n == 1:
    print(0)
    exit()

# b+c >= 2sqrt(bc), a >= 2sqrt(bc), a**2 >= 4bc, (a**2)/4 >= bc -> a가 2*a'일 때, a'**2 >= bc

dp = defaultdict(lambda: -1)
dp[1] = 0
dp[2] = 1

def solve(i):
    if dp[i] != -1:
        return dp[i]

    if i%2 == 0:
        dp[i] =  (i//2)**2 + solve(i//2) * 2
    else:
        r = i/2
        a, b = math.floor(r), math.ceil(r)
        dp[i] = solve(a)+solve(b)+a*b

    return dp[i]


print(solve(n))
