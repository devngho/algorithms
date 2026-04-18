t = int(input())
ns = []

for _ in range(t):
    ns.append(int(input()))

m = max(ns) + 1
primes = set(range(2, m))

for i in range(2, m):
    if i in primes:
        for j in range(i*2, m, i):
            primes.discard(j)

def digits_to_num(n) -> int:
    res = 0
    for i in n:
        res *= 10
        res += i

    return res

cnt = [0]
s = 0
for i in range(1, max(ns)+1):
    digits = list(map(int, list(str(i))))
    is_special = i+1 in primes

    if is_special:
        for j in range(1, len(digits)):
            n = digits_to_num(digits[:j]) * digits_to_num(digits[j:]) + 1
            if n not in primes:
                is_special = False
                break

    if is_special:
        s += 1

    cnt.append(s)

for i in ns:
    print(cnt[i])