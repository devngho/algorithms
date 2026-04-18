def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
gcd_ = gcd(a, b)
lcm = a*b//gcd_

print(gcd_)
print(lcm)