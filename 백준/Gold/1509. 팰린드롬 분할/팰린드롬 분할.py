import sys
from collections import deque


def solve(s: str):
    if len(s) == 0:
        return 0
    elif len(s) == 1:
        return 1

    # find all
    palindromes = {}

    # singles
    for i in range(0, len(s)):
        palindromes[i] = {(i, i)}

    # odds
    for i in range(0, len(s)):
        l, r = i, i
        while l-1 >= 0 and r+1 < len(s):
            if s[l-1] == s[r+1]:
                l-=1
                r+=1
                if l != r:
                    palindromes[l].add((l, r))
            else:
                break

    # evens
    for i in range(0, len(s)-1):
        l, r = i, i+1
        if s[l] != s[r]:
            continue

        palindromes[l].add((l, r))

        while l - 1 >= 0 and r + 1 < len(s):
            if s[l - 1] == s[r + 1]:
                l -= 1
                r += 1
                palindromes[l].add((l, r))
            else:
                break

    palindromes[len(s)] = {(len(s)-1, len(s)-1)}

    queue=deque([(0, 0)]) # pos, cnt
    visited=[sys.maxsize]*(len(s)+1)
    while len(queue) > 0:
        v = queue.popleft()

        for i in palindromes[v[0]]:
            if i[1] == len(s):
                if visited[i[1]] > v[1]+1:
                    visited[i[1]] = v[1]+1
            elif visited[i[1]+1] > v[1]+1:
                queue.append((i[1] + 1, v[1] + 1))
                visited[i[1]+1] = v[1]+1

    return visited[-1]

inp=input()
print(solve(inp))
