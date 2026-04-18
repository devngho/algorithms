a,b=list(map(int, input().split(' : '))),list(map(int, input().split(' : ')))
t2 = b[0]*3600 + b[1]*60 + b[2]
if a[0] > b[0] or (a[0] == b[0] and (a[1] > b[1] or (a[1] == b[1] and a[2] > b[2]))): # a > b
    t1 = 86400 - (a[0]*3600) - (a[1]*60) -a[2]
    print(t1+t2)
else:
    t1 = a[0]*3600 + a[1]*60 + a[2]
    print(t2-t1)