n, y, x = map(int, input().split())
pos = 0 # left top

x, y = x+1, y+1

while n != 0:
    w = 2 ** n // 2 # 한 사분면의 w
    up = y <= w
    left = x <= w
    
    a = w ** 2
    if up and not left:
        # 제1사분면
        x -= w
        pos += a
    elif up and left:
        # 제2사분면
        pass
    elif not up and left:
        #제3
        y -= w
        pos += a * 2
    else:
        #제4
        x -= w
        y -= w
        pos += a * 3

    n -= 1

print(pos)