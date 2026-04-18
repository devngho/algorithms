inp = int(input())

dp = [0] * (inp + 1)

for i in range(2, inp+1):
    cases = [dp[i-1] + 1]
    if i % 3 == 0: cases.append(dp[i//3] + 1)
    if i % 2 == 0: cases.append(dp[i//2] + 1)
    dp[i] = min(cases)
    
print(dp[inp])