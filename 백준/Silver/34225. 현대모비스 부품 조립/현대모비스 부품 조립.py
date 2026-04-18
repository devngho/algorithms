n = int(input())
arr = list(map(int, input().split()))
idx = list(sorted(list(range(n)), key=lambda x: arr[x]))

modules = []
latest_module = 0
score = 0
max_score = 0
max_idx = 0

while len(modules) < n:
    k = idx[-1]

    v = arr[k]
    score_delta = (v-latest_module)+v

    del idx[-1]
    modules.append(k + 1)

    score += score_delta
    latest_module = v

    if score > max_score:
        max_idx = len(modules)
        max_score = score

print(len(modules[:max_idx]))
print(*modules[:max_idx],sep=' ')