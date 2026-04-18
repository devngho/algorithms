import sys
from itertools import combinations
from typing import Tuple, List, Dict, Set

n, m = map(int, input().split())
arr = [input().split() for _ in range(n)]


chickens: Set[Tuple[int, int]] = set()
distances: Dict[Tuple[int, int], Dict[Tuple[int, int], int]] = {} # houses and its distance to each chicken

for y in range(n):
    for x in range(n):
        if arr[y][x] == '2':
            chickens.add((x, y))
        elif arr[y][x] == '1':
            distances[(x, y)] = {}

for (x, y) in chickens:
    for (i, j) in distances.keys():
        distances[(i, j)][(x, y)] = abs(x-i) + abs(y-j)

res = sys.maxsize

for i in combinations(chickens, m):
    city = 0

    for _, v in distances.items():
        city += min(v.items(), key=lambda r: r[1] if r[0] in i else sys.maxsize)[1]

    if city < res:
        res = city

print(res)