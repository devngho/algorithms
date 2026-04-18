def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a%b)

x, y = map(int, input().split())
r = gcd(x, y)
print((x*y)//r)