n, k = map(int, input().split())
l = [int(input()) for _ in range(n)]

cnt = 0

for i in reversed(l):
    cnt += k //i
    k = k % i
    if k == 0: break

print(cnt)
