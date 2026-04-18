n,inp=int(input()),input()
d,m=map(int,input().split())

pending_chars=0
energy=0
h,y,u=0,0,0

for c in inp:
    if c == 'H' or c == 'Y' or c == 'U':
        if c == 'H':
            h+=1
        elif c == 'Y':
            y+=1
        elif c == 'U':
            u+=1
        
        if pending_chars >= 1:
            energy+=min(d+m, d*pending_chars)
            pending_chars=0
    else:
        pending_chars+=1

if pending_chars >= 1:
    energy+=min(d+m, d*pending_chars)

print('Nalmeok' if energy == 0 else energy)
cnt=min(h,y,u)
print('I love HanYang University' if cnt == 0 else cnt)