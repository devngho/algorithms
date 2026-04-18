from collections import deque

t = int(input())

for _ in range(t):
    func = input()
    input()
    arr_ = input()
    arr = deque(map(int, arr_.strip('[]').split(','))) if arr_ != "[]" else []

    is_reversed = False
    is_ok = True

    for i in func:
        if i == 'R': is_reversed = not is_reversed
        elif len(arr) == 0:
            is_ok = False
            print('error')
            break
        elif is_reversed: arr.pop()
        else: arr.popleft()

    if not is_ok: continue
    elif is_reversed: print(f'[{",".join(map(str, reversed(arr)))}]')
    else: print(f'[{",".join(map(str, arr))}]')