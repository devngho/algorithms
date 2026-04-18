import sys
from collections import defaultdict

_, arr = sys.stdin.readline(), list(map(int, sys.stdin.readline().split()))

palindromes = defaultdict(set)

# odds
for i in range(0, len(arr)):
    l, r = i, i
    while l-1 >= 0 and r+1 < len(arr):
        if arr[l - 1] == arr[r + 1]:
            l-=1
            r+=1
            palindromes[l].add(r)
        else:
            break

# evens
for i in range(0, len(arr) - 1):
    l, r = i, i+1
    if arr[l] != arr[r]:
        continue

    palindromes[l].add(r)

    while l - 1 >= 0 and r + 1 < len(arr):
        if arr[l - 1] == arr[r + 1]:
            l -= 1
            r += 1
            palindromes[l].add(r)
        else:
            break

res=[]

for _ in range(int(input())):
    s, e = map(int, sys.stdin.readline().split())

    res.append("1" if s==e or e-1 in palindromes[s-1] else "0")

print('\n'.join(res))