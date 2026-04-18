a,b,c,d=map(int,input().split())
p,n,m=map(int,input().split())

d1, d2 = a+b, c+d

print((1 if 0<(p%d1)<=a else 0) + (1 if 0<(p%d2)<=c else 0))
print((1 if 0<(n%d1)<=a else 0) + (1 if 0<(n%d2)<=c else 0))
print((1 if 0<(m%d1)<=a else 0) + (1 if 0<(m%d2)<=c else 0))