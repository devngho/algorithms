import math

m, n = map(int, input().split())

arr = range(max(2, m), n + 1)

for i in range(2, int(math.sqrt(n)) + 1):
    arr = list(filter(lambda x: x % i != 0 or x == i, arr))

print('\n'.join(map(str, arr)))