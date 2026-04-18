n = int(input())

d = [0] * 10001

for _ in range(n): d[int(input())] += 1

for k in range(10001):
    for _ in range(d[k]): print(k)