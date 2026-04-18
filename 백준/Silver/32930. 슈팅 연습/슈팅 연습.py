n,m=map(int,input().split())
targets = [tuple(map(int, input().split())) for _ in range(n)]
targets_will_appear = [tuple(map(int, input().split())) for _ in range(m)]

pos = (0, 0)
score = 0
distance = lambda x: (pos[0]-x[0])**2+(pos[1]-x[1])**2

for i in range(m):
    target = max(targets, key=distance)
    score += distance(target)
    pos = target
    targets.remove(target)
    targets.append(targets_will_appear[i])

print(score)