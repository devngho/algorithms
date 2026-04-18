n=int(input())-7
arr=[input() for _ in range(7)]
arr=[(i, float(i)) for i in arr]
arr.sort(key=lambda x: x[1])
criteria = arr[-1][1]

for _ in range(n):
    v = input()
    vv = float(v)
    if vv < criteria:
        del arr[-1]
        arr.append((v, vv))
        arr.sort(key=lambda x: x[1])
        criteria = arr[-1][1]

print(*map(lambda x: x[0], arr), sep='\n')