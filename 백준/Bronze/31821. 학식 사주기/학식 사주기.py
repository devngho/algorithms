menu=[int(input()) for _ in range(int(input()))]
print(sum(map(lambda _: menu[int(input())-1], range(int(input())))))