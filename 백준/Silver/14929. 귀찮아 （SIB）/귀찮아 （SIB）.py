s=0
l=None
_=input()
for i in map(int, input().split()):
    if l != None:
        s+=i*l
        l+=i
    else:
        l=i
print(s)