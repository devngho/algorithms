a,b=map(int,input().split())
for _ in range(int(input())):
    x=int(input())
    if x <= 1000:
        print(x, a*x)
    else:
        print(x, 1000*a+b*(x-1000))