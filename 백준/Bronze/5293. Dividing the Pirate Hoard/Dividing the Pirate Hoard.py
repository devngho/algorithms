m, n = map(int, input().split())
res=[]

for _ in range(n):
    x = m%n+m//n
    m-=x
    res.append(x)

print(*res)
print(m)