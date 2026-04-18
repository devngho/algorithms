n, a, b = int(input()), list(input().split()), list(input().split())

if a != b[:n]: print('NO')
elif len(set(b)-set(a)) != 0: print('NO')
else: print('YES')