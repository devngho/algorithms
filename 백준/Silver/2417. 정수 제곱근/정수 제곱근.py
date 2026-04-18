import math
n=int(input())
r=math.isqrt(n)
if r**2 != n:
    print(r+1)
else:
    print(r)