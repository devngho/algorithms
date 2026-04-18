n, m = map(int, input().split())
words = {}

for _ in range(n):
    q, a = input().split()
    words[q] = a

for _ in range(m):
    s = input()

    matched = []
    for i in range(len(s)):
        m = []
        for j in range(1, min(11, len(s)-i+1)):
            t=s[i:i+j]
            # print(t, j)
            if t in words:
                m.append((t, words[t]))
        for j in map(lambda x: x[1], sorted(m, key=lambda x: x[0])):
            matched.append(j)

    if len(matched) > 0:
        print(''.join(matched))
    else:
        print(-1)