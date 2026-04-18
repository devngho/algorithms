w, h = [int(i) for i in input().split()]
maps = [input() for i in range(w)]

min_no_matches = 64

for x in range(w-7):
    for y in range(h-7):
        submap = list(map(lambda x: x[y:y+8],maps[x:x+8]))
        no_matches_wb = 0
        no_matches_bw = 0
        for iy, xx in enumerate(submap):
            for ix, yy in enumerate(list(xx)):
                if (ix + iy) % 2 == 0 and yy == 'B' or (ix + iy) % 2 == 1 and yy == 'W':
                    no_matches_wb += 1
                if (ix + iy) % 2 == 0 and yy == 'W' or (ix + iy) % 2 == 1 and yy == 'B':
                    no_matches_bw += 1
        if min_no_matches > no_matches_wb:
            min_no_matches = no_matches_wb
        if min_no_matches > no_matches_bw:
            min_no_matches = no_matches_bw

print(min_no_matches)