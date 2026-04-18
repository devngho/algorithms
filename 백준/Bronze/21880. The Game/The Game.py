a,b=map(int,input().split())
x,y=0,0

if a>b:
    for _ in range(b):
        y+=1
        print(f"{x}:{y}")
    for _ in range(a):
        x+=1
        print(f"{x}:{y}")
else:
    for _ in range(a):
        x+=1
        print(f"{x}:{y}")
    for _ in range(b):
        y+=1
        print(f"{x}:{y}")