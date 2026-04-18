n=int(input())
arr=[list(input()) for _ in range(n)]

possible_swaps = []

for y in range(n):
    for x in range(n):
        if x < n-1:
            if arr[y][x] != arr[y][x+1]:
                possible_swaps.append(((y, x), (y, x+1)))
        if y < n-1:
            if arr[y][x] != arr[y+1][x]:
                possible_swaps.append(((y, x), (y+1, x)))

max_line = -1

for j in range(n):
    last = ''
    length = 0
    for k in range(n):
        cur = arr[j][k]

        if last == cur:
            length += 1
        else:
            if length > max_line:
                max_line = length
            last = cur
            length = 1

    if length > max_line:
        max_line = length

for j in range(n):
    last = ''
    length = 0
    for k in range(n):
        cur = arr[k][j]

        if last == cur:
            length += 1
        else:
            if length > max_line:
                max_line = length
            last = cur
            length = 1

    if length > max_line:
        max_line = length

for i in possible_swaps:
    affected_rows = {i[0][0], i[1][0]}
    affected_cols = {i[0][1], i[1][1]}

    for j in affected_rows:
        last = ''
        length = 0

        for k in range(n):
            cur = ''
            if (j, k) == i[0]:
                cur = arr[i[1][0]][i[1][1]]
            elif (j, k) == i[1]:
                cur = arr[i[0][0]][i[0][1]]
            else:
                cur = arr[j][k]

            if last == cur:
                length += 1
            else:
                if length > max_line:
                    max_line = length
                last = cur
                length = 1

        if length > max_line:
            max_line = length


    for k in affected_cols:
        last = ''
        length = 0

        for j in range(n):
            cur = ''
            if (j, k) == i[0]:
                cur = arr[i[1][0]][i[1][1]]
            elif (j, k) == i[1]:
                cur = arr[i[0][0]][i[0][1]]
            else:
                cur = arr[j][k]

            if last == cur:
                length += 1
            else:
                if length > max_line:
                    max_line = length
                last = cur
                length = 1

        if length > max_line:
            max_line = length

print(max_line)