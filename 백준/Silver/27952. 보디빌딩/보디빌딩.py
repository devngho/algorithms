n,x=map(int,input().split())
a,b=list(map(int,input().split())),list(map(int,input().split()))
weight=0
okay=True
for i in range(n):
    weight += b[i]
    if weight < a[i]:
        okay=False
        break

if okay:
    print((weight-a[-1])//x)
else:
    print(-1)