to_find = int(input())
i, n = 666, 0
while True:
    if "666" in str(i):
        n += 1
    if n == to_find:
        print(i)
        break
    i += 1
