a = int(input())
b = int(input())
lanes = []
for i in reversed(str(b)):
    i = int(i)
    lanes.append(str(a * i))
for i in lanes:
    print(i)
print(a * b)
