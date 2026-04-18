for i in [input() for _ in range(int(input()))]:
    n = 0
    ok = True

    for j in i:
        if j == '(': n += 1
        else: n -= 1

        if n < 0:
            ok = False
            break
    ok = ok and n == 0

    print('YES' if ok else 'NO')