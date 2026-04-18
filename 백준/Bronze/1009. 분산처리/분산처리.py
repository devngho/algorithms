for i in range(int(input())):
    a, b = map(int, input().split())
    res=1
    for _ in range(b):
        res *= a
        res %= 10
    print(res if res != 0 else 10)