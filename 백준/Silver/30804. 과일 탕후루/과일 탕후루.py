from collections import defaultdict

n, arr = int(input()), list(map(int, input().split()))

l, r, max_len = 0, 0, 0
cur_cnt = defaultdict(lambda: 0)
cur = set()

while l < n-1 and r <= n:
    if len(cur) <= 2:
        if max_len < r-l:
            max_len = r-l

        if r < n:
            cur_cnt[arr[r]] += 1
            cur.add(arr[r])
            r+=1
        else:
            break
    else:
        if cur_cnt[arr[l]] != 0:
            cur_cnt[arr[l]] -= 1

        if cur_cnt[arr[l]] == 0:
            cur.remove(arr[l])

        l+=1

if n == 1:
    print(1)
else:
    print(max_len)