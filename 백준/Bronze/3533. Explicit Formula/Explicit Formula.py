from itertools import chain

x = list(map(int, input().split()))
pairs = chain(*[[1 if (x[a] or x[b]) else 0 for b in range(a, 10)] for a in range(10)])
triplets = chain(*chain(*[[[1 if x[a] or x[b] or x[c] else 0 for c in range(b, 10)] for b in range(a, 10)] for a in range(10)]))

print((sum(pairs) + sum(triplets)) % 2)