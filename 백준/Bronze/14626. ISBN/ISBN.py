isbn = list(input())
m = int(isbn[-1])

idx = 0
total = 0
for i, v in enumerate(isbn[:-1]):
    if v == '*':
        idx = i
        continue
    
    if i % 2 == 0:
        total += int(v)
    else:
        total += 3 * int(v)

w = 1 if idx % 2 == 0 else 3
for i in range(10):
    if (total + i * w + m) % 10 == 0:
        print(i)
