inp = int(input())

dp = [0] * (inp + 1)
path = [[i] for i in range(0, inp + 2)]

for i in range(2, inp + 1):
    cases = [(dp[i - 1] + 1, path[i-1] + [i])]
    if i % 3 == 0: cases.append((dp[i // 3] + 1, path[i//3]+[i]))
    if i % 2 == 0: cases.append((dp[i // 2] + 1, path[i//2]+[i]))
    m = min(cases, key=lambda x: x[0])
    dp[i] = m[0]
    path[i] = m[1]

print(dp[inp])
print(' '.join(map(str,reversed(path[inp]))))