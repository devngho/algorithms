from math import sqrt

xA, yA, xB, yB, xC, yC = map(int, input().split())

dx, dy = xA - xB, yA - yB
dx_, dy_ = xA - xC, yA - yC

if (dy == 0 and dy_ == 0) or (dy != 0 and dy_ != 0 and dx/dy == dx_/dy_):
    print(-1.0)
else:
    xD1, yD1 = xC + dx, yC + dy
    xD2, yD2 = xC - dx, yC - dy
    xD3, yD3 = xB + dx_, yB + dy_

    AB = sqrt((xA - xB) ** 2 + (yA - yB) **2)
    BC = sqrt((xB - xC) ** 2 + (yB - yC) **2)
    AC = sqrt((xA - xC) ** 2 + (yA - yC) **2)
    AD1 = sqrt((xA - xD1) ** 2 + (yA - yD1) **2)
    CD1 = sqrt((xC - xD1) ** 2 + (yC - yD1) **2)
    BD2 = sqrt((xB - xD2) ** 2 + (yB - yD2) **2)
    CD2 = sqrt((xC - xD2) ** 2 + (yC - yD2) **2)
    AD3 = sqrt((xA - xD3) ** 2 + (yA - yD3) ** 2)
    BD3 = sqrt((xB - xD3) ** 2 + (yB - yD3) ** 2)

    c1 = AB + BC + AD1 + CD1
    c2 = AB + AC + BD2 + CD2
    c3 = AC + BC + AD3 + BD3

    print(max([c1, c2, c3]) - min([c1, c2, c3]))
