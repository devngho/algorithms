_, m = map(int, input().split())
nums = list(map(int, input().split()))
max_sum = 0
for ia, a in enumerate(nums):
    for ib, b in enumerate(nums):
        if ia == ib: continue
        for ic, c in enumerate(nums):
            if ia == ic or ib == ic: continue
            if max_sum < a + b + c <= m:
                max_sum = a + b + c

print(max_sum)