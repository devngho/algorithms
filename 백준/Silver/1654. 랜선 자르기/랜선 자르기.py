def solve(n, lines):
    a = 0
    b = max(lines)+1
    mid = (a + b) // 2

    while a != b:
        mid_cnt = sum([i // mid for i in lines])

        if mid_cnt >= n:
            a = mid + 1
        else:
            b = mid
        mid = (a + b) // 2

    return b - 1


k_, n_ = map(int, input().split())
lines_ = [int(input()) for _ in range(k_)]

res = solve(n_, lines_)
print(res)