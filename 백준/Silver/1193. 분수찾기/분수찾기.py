x=int(input())
i=1
c=1

while i < x:
    c += 1
    i += c
d=i-x

if c % 2 == 0:
    print(f"{c-d}/{d+1}")
else:
    print(f"{d+1}/{c-d}")