_,m=map(int,input().split())
arr=[tuple(input().split()) for _ in range(m)]
arr.sort(key=lambda x: int(x[0]))
arr.sort(key=lambda x: int(x[1]))
print(''.join(map(lambda x: x[2], arr)))