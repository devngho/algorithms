from collections import deque

inp = deque([int(input()) for _ in range(int(input()))])
arr = deque(range(1, len(inp) + 1))
stack = deque()
task = []

while len(inp) != 0:
    while (len(stack) == 0 or stack[-1] != inp[0]) and not len(arr) == 0:
        stack.append(arr.popleft())
        task.append('+')

    if stack[-1] != inp[0]:
        task = ['NO']
        break

    while len(stack) != 0 and stack[-1] == inp[0]:
        stack.pop()
        inp.popleft()
        task.append('-')


print('\n'.join(task))