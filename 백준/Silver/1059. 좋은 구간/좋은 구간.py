_, s, n = input(), [0] + list(map(int, input().split())), int(input())

good_ranges = 0
for b in range(max(s)):
    for a in range(b):
        if a <= n <= b:
            no_i = False
            for i in range(a, b + 1):
                if i in s:
                    no_i = True
                    break
            if not no_i:
                good_ranges += 1
                # print(f"[{a}, {b}]")

print(good_ranges)
