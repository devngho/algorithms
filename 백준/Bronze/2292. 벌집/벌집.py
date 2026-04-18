def solve(x):
    if x == 1:
        return 1

    i = 0
    a = 0

    while True:
        i += 1
        a += 6 * i
        if x <= a+1:
            return i + 1


inp = int(input())
res = solve(inp)
print(res)