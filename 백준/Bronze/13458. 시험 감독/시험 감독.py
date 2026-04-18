import math

_=input()
arr=list(map(int, input().split()))
a,b=map(int,input().split())

total=0
for i in arr:
    if i <= a:
        total+=1
    else:
        total+=1+math.ceil(float(i-a)/b)
        
print(total)