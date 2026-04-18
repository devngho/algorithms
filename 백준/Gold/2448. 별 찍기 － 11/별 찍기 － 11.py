n = int(input())
arr = [[False] * (n*2) for _ in range(n)]

def draw(x, y, n):
    if n < 3:
        return
    
    for i in range(n-1):
        arr[y+i][x+n-i-1]=True
        arr[y+i][x+n+i-1]=True
    for i in range(2*n-1):
        arr[y+n-1][x+i]= i != n-1 or n==3
    
    draw(x+n//2, y, n//2)
    draw(x, y+n//2, n//2)
    draw(x+n, y+n//2, n//2)

draw(0, 0, n)

print('\n'.join(map(lambda x: ''.join(map(lambda x: '*' if x else ' ', x)), arr)))