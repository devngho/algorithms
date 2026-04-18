a=input()
print(sum(map(lambda x:0 if 'SciComLove'[x]==a[x] else 1, range(10))))