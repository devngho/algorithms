n, l, k = map(int, input().split())
p_ = list(map(int, input().split()))
p = [0] * l

for i in p_:
    p[i-1] = 1

p = p + p

prefix = [0] + [0] * (l * 2)
s = 0
for i in range(l * 2):
    s += p[i]
    prefix[i+1] = s

played_scenes, played_frames, rate = 1, 0, 1

# start: inclusive, end: exclusive
def count_range(start: int, end: int) -> int:
    if end - start >= l:
        cycles = (end-start) // l
        start += cycles * l

        return cycles * k + count_range(start, end)
    else:
        c = (end // l - 1) * l
        start -= c + 1
        end -= c + 1
        # sum(p[start:end])
        return prefix[end] - prefix[start]

while played_scenes < l * n + 1:
    played_frames += 1
    # print(played_frames, played_scenes, rate)
    rate_ = count_range(played_scenes, played_scenes + rate)
    played_scenes += rate
    rate += rate_
    # print(rate)
    # print()

print(played_frames)