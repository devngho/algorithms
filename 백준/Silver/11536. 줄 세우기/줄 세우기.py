arr=[input() for _ in range(int(input()))]
s=sorted(arr)

if arr==list(s): print('INCREASING')
elif arr==list(reversed(s)): print('DECREASING')
else: print('NEITHER')