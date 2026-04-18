arr=list(map(int,input().split(":")))
if any(map(lambda x: x > 59, arr)):
    print(0)
else:
    print(len(list(filter(lambda x: 1<=x<=12, arr)))*2)