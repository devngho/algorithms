n=int(input())
words=list(set([input() for _ in range(n)]))
dict_sorted = sorted(words)
lens = sorted(dict_sorted, key=len)
for w in lens: 
    print(w)