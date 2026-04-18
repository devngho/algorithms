teams = int(input().split()[0])
broken = list(map(lambda x: int(x) - 1, input().split()))
additional = list(map(lambda x: int(x) - 1, input().split()))


def check_and_delete(a, b):
    if a in broken and b in additional:
        broken.remove(a)
        additional.remove(b)


for i in range(teams):
    check_and_delete(i, i)

for i in range(teams):
    check_and_delete(i, i-1)
    check_and_delete(i, i+1)

print(len(broken))
