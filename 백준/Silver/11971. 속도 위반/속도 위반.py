n, m = map(int, input().split())
limits = [tuple(map(int, input().split())) for _ in range(n)]
speeds = [tuple(map(int, input().split())) for _ in range(m)]
limit_cursor = 0
speed_cursor = 0
limit_cumulative = 0 # limits[0][0]
speed_cumulative = 0 # speeds[0][0]
speed = speeds[0][1]
limit = limits[0][1]
max_speeding = max(0, speed - limit)

for i in range(1, 101):
    if i > speed_cumulative:
        speed = speeds[speed_cursor][1]
        speed_cumulative += speeds[speed_cursor][0]
        speed_cursor += 1

    if i > limit_cumulative:
        limit = limits[limit_cursor][1]
        limit_cumulative += limits[limit_cursor][0]
        limit_cursor += 1

    if speed - limit > max_speeding:
        max_speeding = speed - limit

    # print(i, speed, limit, speed_cumulative, limit_cumulative, max_speeding)

print(max_speeding)