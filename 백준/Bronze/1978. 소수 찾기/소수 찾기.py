def is_prime(x: int) -> bool:
    if x == 1:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def solve(x):
    s = x.split()
    cnt = 0
    for ss in s:
        if is_prime(int(ss)):
            cnt += 1
    return cnt


input()
inp = input()
res = solve(inp)
print(res)