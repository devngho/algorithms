r=[6,3,2,1,2]
a,b=map(int,input().split()),map(int,input().split())
print(sum(map(lambda x:x[1]*r[x[0]], enumerate(a))), sum(map(lambda x:x[1]*r[x[0]], enumerate(b))))