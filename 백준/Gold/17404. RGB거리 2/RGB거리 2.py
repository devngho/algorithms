import sys


def solve(x):
    arr=[[*x[i]] for i in range(len(x))]
    temp=[]
    for j in range(3): # decide 0
        arr[0][j]=x[0][j]
        for i in {0, 1, 2} - {j}:
            arr[0][i]=sys.maxsize
        for i in range(1, len(x)):
            arr[i] = [
                min(arr[i-1][1], arr[i-1][2]) + x[i][0],
                min(arr[i-1][0], arr[i-1][2]) + x[i][1],
                min(arr[i-1][0], arr[i-1][1]) + x[i][2],
            ]
        temp.append(min([
            arr[-1][0] if j != 0 else sys.maxsize,
            arr[-1][1] if j != 1 else sys.maxsize,
            arr[-1][2] if j != 2 else sys.maxsize,
        ]))

    return min(temp)


cnt = int(input())
inp = [list(map(int, input().split())) for _ in range(cnt)]
res = solve(inp)
print(res)
