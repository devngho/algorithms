def solve(x):
    old_set = set(x)
    for i in range(len(x[0])):
        new_set = set(map(lambda x: x[i:],old_set))
        if len(old_set) - len(new_set) != 0:
            return len(x[0]) - i + 1
    return 1


cnt = int(input())
lines = [input() for _ in range(cnt)]
res = solve(lines)
print(res)