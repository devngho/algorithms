_,a,_,b=input(),list(sorted(map(int, input().split()))),input(),list(map(int, input().split()))
m={k: False for k in b}
for i in a:
    if i in m:
        m[i]=True
print(' '.join(['1' if m[i] else '0' for i in b]))