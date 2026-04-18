def solve(x, y):
    x = set(map(int, x.split()))
    y = map(int, y.split())
    for yy in y:
        if yy in x:
            print("1")
        else:
            print("0")

input()
a = input()
input()
m = input()
solve(a, m)