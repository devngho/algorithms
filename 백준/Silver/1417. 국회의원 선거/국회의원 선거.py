num = input()
pyo = [int(input()) for num in range(int(num))]


def max_idx(list):
    max = pyo[0]
    idx = 0
    for i, x in enumerate(pyo):
        if x >= max:
            idx, max = i, x
    return idx


def solve():
    if num == "1":
        print(0)
        return
    need_pyo = 0
    while max_idx(pyo) != 0:
        pyo[max_idx(pyo)] -= 1
        need_pyo += 1
        pyo[0] += 1
    print(need_pyo)

solve()