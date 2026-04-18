def solve(x: list[list[int]]):
    for i in range(1, len(x)):
        x[i] = [
            min(x[i-1][1], x[i-1][2]) + x[i][0],
            min(x[i - 1][0], x[i - 1][2]) + x[i][1],
            min(x[i - 1][0], x[i - 1][1]) + x[i][2],
        ]
    return min(x[-1][0], x[-1][1], x[-1][2])


cnt = int(input())
inp = [list(map(int, input().split())) for _ in range(cnt)]
res = solve(inp)
print(res)
