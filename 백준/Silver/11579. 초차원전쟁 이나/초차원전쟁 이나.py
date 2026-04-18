for _ in range(int(input())):
    n = int(input())
    allowed_moves = [list(map(int, input().split())) for _ in range(n)]
    coord = list(map(int, input().split()))

    pos = [0] * n
    cnt = 0

    for i in range(n): # i-th dim
        if pos[i] == coord[i]:
            continue
        elif pos[i] > coord[i]:
            break
        else:
            r = coord[i]-pos[i]
            for j in range(n):
                pos[j] += allowed_moves[i][j] * r
            cnt += r

    if pos != coord or cnt > 2000000000:
        print(0)
    else:
        print(1, cnt)