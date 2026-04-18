n,d=input().split()
print(sum(map(lambda x: str(x).count(d), range(1, int(n)+1))))