arr=[(a, int(b), int(c), int(d)) for (a, b, c, d) in [input().split() for _ in range(int(input()))]]

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[3], reverse=True)
arr.sort(key=lambda x: x[2])
arr.sort(key=lambda x: x[1], reverse=True)

print(*map(lambda x: x[0], arr), sep='\n')