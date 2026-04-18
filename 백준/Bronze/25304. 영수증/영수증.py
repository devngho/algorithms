p=int(input())
v=0
for _ in range(int(input())):
    a,b=map(int, input().split())
    v+=a*b
print("Yes" if p==v else "No")