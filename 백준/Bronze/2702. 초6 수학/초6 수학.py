def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a%b)

for _ in range(int(input())):
    x, y = map(int, input().split())
    r = gcd(x, y)
    print((x*y)//r, r)