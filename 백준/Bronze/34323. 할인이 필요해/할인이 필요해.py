n,m,s=map(int,input().split())
print(min(s*m, s*(100-n)*(m+1)//100))