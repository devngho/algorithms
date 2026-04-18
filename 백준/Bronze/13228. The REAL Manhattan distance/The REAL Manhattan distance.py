for _ in range(int(input())):
    x1,y1,z1,x2,y2,z2=map(int, input().split())
    print(abs(x2-x1)+abs(y2-y1)+z1+z2)