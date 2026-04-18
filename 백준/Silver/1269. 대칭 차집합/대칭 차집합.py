_, a, b = input(), set(input().split()), set(input().split())
print(len((a-b).union(b-a)))