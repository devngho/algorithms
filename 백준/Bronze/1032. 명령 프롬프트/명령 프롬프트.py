n=int(input())
s=list(input())

for _ in range(n-1):
    inp=input()
    for i in range(len(inp)):
        if s[i] != '?' and inp[i] != s[i]:
            s[i]='?'

print(*s,sep='')