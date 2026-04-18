import math

n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(map(lambda x: math.ceil(x / t), shirts)))
print(n // p, n % p)