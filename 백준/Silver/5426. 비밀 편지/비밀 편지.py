import math

for _ in range(int(input())):
    inp=input()
    n=math.isqrt(len(inp))
    for i in range(n-1, -1, -1):
        for j in range(n):
            print(inp[j*n+i],end='')
    print()