n,k=map(int,input().split())
arr=list(map(int, input().split()))

s=sum(arr[:k])
m=s

for i in range(1, n-k+1):
    s -= arr[i-1]
    s += arr[i+k-1]
    if m < s:
        m=s

print(m)