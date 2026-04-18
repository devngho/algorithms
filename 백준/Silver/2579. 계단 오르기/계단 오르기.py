scores = [int(input()) for _ in range(int(input()))]

if len(scores) == 1:
    print(scores[0])
elif len(scores) == 2:
    print(scores[0] + scores[1])
else:
    dp = [scores[0], scores[0] + scores[1], max(scores[0] + scores[2], scores[1] + scores[2])] + [0] * (len(scores) - 3)

    for i in range(len(scores)):
        if i < 3: continue
        dp[i] = max(dp[i-2]+scores[i], dp[i-3] + scores[i-1] + scores[i])

    print(dp[-1])