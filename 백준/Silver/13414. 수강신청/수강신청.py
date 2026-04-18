from collections import defaultdict

k,n = map(int, input().split())
s=0
cnt=defaultdict(lambda: 0)
state=defaultdict(lambda: 0)
q=[]

for i in [input() for _ in range(n)]:
    cnt[i] += 1
    q.append(i)

for i in q:
    state[i] += 1
    if state[i] == cnt[i]:
        print(i)
        s+=1
        if s >= k: break