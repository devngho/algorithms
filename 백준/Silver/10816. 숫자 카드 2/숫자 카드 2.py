input()
cards = list(map(int, input().split()))
input()
to_count = list(map(int, input().split()))

count = {}
for i in cards:
    if i in count: count[i] += 1
    else: count[i] = 1

for i in to_count:
    print(count[i] if i in count else 0, end=' ')