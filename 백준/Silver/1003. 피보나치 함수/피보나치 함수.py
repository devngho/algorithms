cache = {0: (1, 0), 1: (0, 1)}


def fibo_01(x: int):
    if x in cache:
        return cache[x]
    else:
        m1 = fibo_01(x - 1)
        m2 = fibo_01(x - 2)
        cache[x] = (m1[0] + m2[0], m1[1] + m2[1])
        return cache[x]


def solve(x):
    for i in x:
        f = fibo_01(i)
        print(f[0], f[1])


cases = int(input())
inp = [int(input()) for _ in range(cases)]
solve(inp)