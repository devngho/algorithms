earth=0
alien=0
other=0
total=int(input())

for _ in range(total):
    inp=input()
    if 'blue' in inp and 'black' in inp:
        earth += 1
    elif 'white' in inp and 'gold' in inp:
        alien += 1
    else:
        other += 1
        
print(earth/total*100)
print(alien/total*100)
print(other/total*100)