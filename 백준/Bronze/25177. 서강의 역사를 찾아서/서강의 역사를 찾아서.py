_, a, b = input(), list(map(int, input().split())), list(map(int, input().split()))
print(max(max(map(lambda x: x[1]-(0 if x[0] >= len(a) else a[x[0]]), enumerate(b))), 0))