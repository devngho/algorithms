n, m = map(int, input().split())
numbers = [list(input()) for _ in range(n)]
max_area = 0

for s in range(min(n, m)):
    for x in range(m-s):
        for y in range(n-s):
            if numbers[y][x] == numbers[y+s][x] == numbers[y][x+s] == numbers[y+s][x+s]:
                max_area = max(max_area, (s+1)*(s+1))

print(max_area)