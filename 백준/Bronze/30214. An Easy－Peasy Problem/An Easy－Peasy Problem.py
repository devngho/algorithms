a, b = map(int, input().split())
b-=a
if a >= b:
    print('E')
else:
    print('H')