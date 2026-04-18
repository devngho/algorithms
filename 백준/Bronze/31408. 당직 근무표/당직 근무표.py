n=int(input())
p=input().split()
cnt={}
max_cnt = 0
for k in p:
    if k in cnt:
        cnt[k] += 1
    else:
        cnt[k] = 1
    
    if max_cnt < cnt[k]:
            max_cnt = cnt[k]

print('YES' if ((n%2==0 and max_cnt <= n//2) or (n%2==1 and max_cnt <= n//2+1)) else 'NO')