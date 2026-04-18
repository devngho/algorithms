def solve(start_idx: int, arr: list[int], m: int):
    if m == 0: return []
    if m == 1: return [[arr[i]] for i in range(start_idx, len(arr))]
    if start_idx > len(arr): return []

    return [[arr[start_idx]] + i for i in solve(start_idx, arr, m-1)] +\
            solve(start_idx+1, arr, m)

n, m = map(int, input().split())
inp=list(sorted(set(map(int, input().split()))))
arr=solve(0, inp, m)

for i in arr:
    print(*i)