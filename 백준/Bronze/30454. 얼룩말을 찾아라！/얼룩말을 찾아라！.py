n, l = map(int, input().split())
m, mn = 0, 0

for _ in range(n):
    inp = input()
    c = 1 if inp[0] == '1' else 0
    for i in range(1,l):
        if inp[i] == '1' and inp[i-1] == '0':
            c += 1
    
    if c > m:
        m, mn = c, 1
    elif m == c:
        mn += 1

print(m, mn)