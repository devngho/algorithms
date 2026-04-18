last_used={}

for i in range(int(input())):
    last_used[input()] = i
    
pinned = {input() for _ in range(int(input()))}

if len(pinned) > 0: print(*sorted(pinned, key=lambda x: last_used[x], reverse=True), sep='\n')
print(*sorted(set(last_used.keys())-pinned, key=lambda x: last_used[x], reverse=True), sep='\n')