cnt=0
sh,sm=map(int,input().split())
eh,em=map(int,input().split())
n=input()
for h in range(sh, eh+1):
    for m in range(0 if h != sh else sm, 60 if h != eh else (em+1)):
        cnt += 1 if n in f"{h:02}{m:02}" else 0

print(cnt)