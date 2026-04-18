import sys

n, s = map(int, input().split())
arr = list(map(int, input().split()))

if sum(arr) < s:
    print(0)
    sys.exit(0)

right = 0
total = arr[0]
m = n

for left in range(n):
    if left > 0: total -= arr[left-1]
    if left > right:
        total = arr[left]
        right = left

    if total == s: pass
    elif total > s:
        while total > s and right >= left:
            total -= arr[right]
            right -= 1

        if total < s:
            right += 1
            total += arr[right]
    else:
        while total < s and right < n-1:
            right += 1
            total += arr[right]

    if total < s: continue

    l = right - left + 1
    if l < m: m = l

print(m)