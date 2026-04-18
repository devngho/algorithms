t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    r = r1 + r2
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif r2 > d + r1 or r1 > d + r2: # one contains the other
        print(0)
    elif r2 == d + r1 or r1 == d + r2: # the inner meets the outer
        print(1)
    elif r > d:
        print(2)
    elif r == d:
        print(1)
    else:
        print(0)