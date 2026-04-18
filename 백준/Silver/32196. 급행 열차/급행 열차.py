n, m, k, x, y = map(int, input().split())
arr=[tuple(map(int,input().split())) for _ in range(n)]
factor=sorted(map(lambda t: t[0]*x-t[1]*y,arr))
print(k*(x+y)+sum(list(factor)[:m]))