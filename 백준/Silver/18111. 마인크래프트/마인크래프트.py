h, w, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]
arr_cnt = {i: 0 for i in range(257)}
M, m = 0, 256

for i in arr:
    for j in i:
        arr_cnt[j] += 1
        if j > M: M = j
        if m > j: m = j

excavation_cnt = [0 for _ in range(258)]

for i in range(M, m-1, -1):
    excavation_cnt[i] = arr_cnt[i] + excavation_cnt[i+1]

place_cnt = [0 for _ in range(258)]

for i in range(m, M+1):
    place_cnt[i] = arr_cnt[i] + place_cnt[i-1]

M_height, m_time = 0, h*w*256

for i in range(M, m-1, -1): # adjust to i
    e = sum(excavation_cnt[i+1:])
    blocks = e + b
    to_fill = sum(place_cnt[:i])

    # print(i, e, to_fill, blocks)
    
    if blocks >= to_fill:
        time = e * 2 + to_fill

        # print(i, e, to_fill, blocks, time)

        if time >= m_time: continue
        
        M_height = i
        m_time = e * 2 + to_fill

print(m_time, M_height)
