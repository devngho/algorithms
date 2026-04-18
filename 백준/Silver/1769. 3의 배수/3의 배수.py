a = int(input())
i = 0

while len(str(a)) != 1:
    i += 1
    a = sum(map(int, list(str(a))))

print(i)
if a % 3 == 0:
    print("YES")
else:
    print("NO")
