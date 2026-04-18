s=-1
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    score = max(arr[:2]) + sum(list(sorted(arr[2:],reverse=True))[:2])
    if s < score:
        s=score
print(s)