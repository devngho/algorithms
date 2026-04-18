from collections import defaultdict

n, m = map(int, input().split())
cnt = defaultdict(lambda: 0)

for _ in range(n):
    word = input()
    if len(word) < m:
        continue
    cnt[word] += 1

words=list(cnt.keys())
words.sort()
words.sort(key=lambda x: len(x),reverse=True)
words.sort(key=lambda x: cnt[x],reverse=True)

print(*words,sep='\n')