_, k = map(int, input().split())
days = list(map(int, input().split()))

max_s = sum(days[:k])
for i in range(len(days)-k+1):
    v = sum(days[i:i+k])
    if max_s < v:
        max_s = v

print(max_s)
