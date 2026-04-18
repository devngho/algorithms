n,k=map(int,input().split())
arr=list(map(int,input().split()))*2
c=sum(arr[:k])
m=c
for i in range(0, n):
    c-=arr[i]
    c+=arr[i+k]
    if c > m: m=c
print(m)