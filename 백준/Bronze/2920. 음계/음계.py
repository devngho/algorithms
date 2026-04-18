def solve(x):
    if x == [1, 2, 3, 4, 5, 6, 7, 8]:
        return 'ascending'
    elif x == [8, 7, 6, 5, 4, 3, 2, 1]:
        return 'descending'
    else:
        return 'mixed'


inp = list(map(int, input().split()))
res = solve(inp)
print(res)
