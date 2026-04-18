n,k=map(int, input().split())
arr=list(map(int, input().split()))
ok,actions=True,0
for i in range(1,n):
    if arr[i-1] >= arr[i]:
        arr[i] += k
        actions += 1
    
    if arr[i-1] >= arr[i]:
        ok=False
        break
if ok:
    print(actions)
else:
    print(-1)