h, w = map(int, input().split())
arr = [[x.count('9') for x in input().split()] for _ in range(h)]

total = sum([sum(x) for x in arr])
max_line = 0

for y in range(h):
    s = sum(arr[y])
    if max_line < s:
        max_line = s

for x in range(w):
    s = sum([arr[i][x] for i in range(h)])
    if max_line < s:
        max_line = s

print(total-max_line)