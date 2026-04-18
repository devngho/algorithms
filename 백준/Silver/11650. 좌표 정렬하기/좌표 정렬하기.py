def solve(x):
    return sorted(sorted(x, key=lambda i: i[1]), key=lambda i: i[0])


inp = int(input())
coords = [list(map(int, input().split())) for _ in range(inp)]
res = solve(coords)
print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', res)))