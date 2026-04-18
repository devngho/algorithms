from collections import defaultdict

n=int(input())
a=defaultdict(lambda:0)

for i in input().split():
    a[i] += 1
    
for i in input().split():
    a[i] -= 1

s=0
for (k, v) in a.items():
    if v < 0:
        s += abs(v)

print(s)