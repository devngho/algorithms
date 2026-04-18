x,y=map(int, input().split())

if x == 0 and y == 0:
    a, b = 125, 125
elif x == 125 and y == 125:
    a, b = 0, 0
elif x == 250:
    a, b = 0, 125
elif y == 250:
    a, b = 125, 0
elif x == 125:
    a, b = 0, 250
elif y == 125:
    a, b = 250, 0
elif x == 0 and y < 125:
    # find x coord(->a) of intersection point where (area)=(250)^2/2
    # a(250-x)=31250, a=31250/(250-x)
    a=31250/(250-y)
    b=-a+250 # y=-x
elif x == 0 and y > 125:
    a=31250/y
    b=0
elif y == 0 and x < 125:
    # find y coord
    b = 31250 / (250 - x)
    a = -b + 250  # y=-x
elif y == 0 and x > 125:
    b = 31250 / x
    a=0
elif x >= 125:
    # find y coord of the point where the line intersects to x=0
    # x(250-b)=31250, 250x-bx=31250, -bx=31250-250x, bx=250x-31250
    b = 250-(31250/x)
    a = 0
else:
    a = 250 - (31250 / y)
    b = 0

print(f"{a:.2f} {b:.2f}")