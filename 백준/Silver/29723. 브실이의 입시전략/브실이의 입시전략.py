n, m, k = map(int, input().split())
subjects = {}

for _ in range(n):
    i, j = input().split()
    subjects[i] = int(j)

known = {input() for _ in range(k)}
known_score = sum([subjects[k] for k in known])
keys = list(sorted(set(subjects.keys()) - known, key=lambda x: subjects[x]))
cnt = m-len(known)

min_score = sum(map(lambda x: subjects[x], list(keys)[:cnt]))
max_score = sum(map(lambda x: subjects[x], list(keys)[-cnt:])) if cnt != 0 else 0

print(min_score + known_score, max_score + known_score)