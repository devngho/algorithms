s = list(input())


def solve():
    change = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            change += 1

    print((change + 1) // 2)


solve()
