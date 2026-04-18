n, m, s = int(input()), int(input()), input()

arr = []
idx = 0
tmp = 0

while idx < m:
    # print(s[idx], tmp)
    if s[idx] == 'I':
        if idx < m-1 and s[idx] == 'I' and s[idx+1] == 'O':  # IO
            tmp += 1
        else: # IO_I_
            arr.append(tmp)
            tmp = 0
    else:
        if (idx < m-1 and s[idx+1] == 'O') or idx == m-1: # OO
            arr.append(tmp-1)
            tmp = 0
        else: # OI
            pass

    idx += 1
# print(arr)

print(sum(map(lambda x: x-n+1, filter(lambda x: x >= n, arr))))