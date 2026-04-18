n,arr=int(input()), list(map(int, input().split()))
print(max(map(lambda x: x[1]-(n-x[0]), enumerate(arr))))