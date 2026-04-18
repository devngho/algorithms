ok = True
input()

used_tiles = []

tiles_near = {1: [2, 4, 5, 6, 8], 2: [1, 3, 4, 5, 6, 7, 9], 3: [2, 4, 5, 6, 8], 4: [1, 2, 3, 5, 7, 8, 9], 5: [1, 2, 3, 4, 6, 7, 8, 9], 6: [1, 2, 3, 5, 7, 8, 9], 7: [2, 4, 5, 6, 8], 8: [1, 3, 4, 5, 6, 7, 9], 9: [2, 4, 5, 6, 8]}
diag = {1: 9, 3: 7, 7: 3, 9: 1}
line = {1: {2: 3, 4: 7}, 2: {5: 8}, 3: {2: 1, 6: 9}, 4: {5: 6}, 5: {}, 6: {5: 4}, 7: {4: 1, 8: 9}, 8: {5: 2}, 9: {6: 3, 8: 7}}

def possible_tiles(i):
    res = set(tiles_near[i])
    
    if 5 in used_tiles and i in diag:
        res.add(diag[i])
    
    for j in line[i].keys():
        if j in used_tiles:
            res.add(line[i][j])
    
    return res

for i in map(int, input().split()):
    if len(used_tiles) != 0 and (i not in possible_tiles(used_tiles[-1]) or i in used_tiles):
        ok = False
        break
    
    used_tiles.append(i)
    
print('YES' if ok else 'NO')