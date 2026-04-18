def solve(x):
    avg = round(sum(x) / len(x))
    mid = sorted(x)[len(x)//2]

    shown_count = {a: x.count(a) for a in set(x)}
    max_shown_count = max(shown_count.values())
    max_shown = sorted(set(filter(lambda i: shown_count[i] == max_shown_count, x)))

    if len(max_shown) >= 2:
        max_shown = max_shown[1]
    else:
        max_shown = max_shown[0]

    rng = max(x) - min(x)

    return avg, mid, max_shown, rng


inp = int(input())
nums = [int(input()) for _ in range(inp)]
res = solve(nums)

print('\n'.join(map(str, res)))
