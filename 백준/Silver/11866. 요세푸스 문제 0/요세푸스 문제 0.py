from collections import deque

n, k = map(int, input().split())
people = deque(range(1, n+1))
order = []
idx = 0

while len(people) != 0:
    idx += 1
    if idx % k != 0:
        people.append(people.popleft())
    else:
        order.append(people.popleft())

print(f"<{', '.join(map(str, order))}>")