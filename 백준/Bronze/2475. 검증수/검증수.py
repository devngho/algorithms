def solve(x):
    return sum(map(lambda i: i**2, x)) % 10


inp = map(int, input().split())
res = solve(inp)
print(res)