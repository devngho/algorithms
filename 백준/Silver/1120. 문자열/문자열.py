def calc_diff(x: str, y: str):
    diff = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            diff += 1
    return diff


def solve(x):
    left, right = x.split()
    diff = len(right) - len(left)
    if diff == 0:
        return calc_diff(left, right)
    min_diff = len(right)
    min_diff_str = ""
    for i in range(0, len(right) - len(left) + 1):
        new_str = list(right)
        for j in range(len(left)):
            new_str[i+j] = left[j]
        new_str = ''.join(new_str)
        # print(new_str, end=' ')
        new_diff = calc_diff(new_str, right)
        # print(new_diff)
        if min_diff > new_diff:
            min_diff = new_diff
            min_diff_str = new_str

    return min_diff


inp = input()
res = solve(inp)
print(res)