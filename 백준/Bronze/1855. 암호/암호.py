n=int(input())
s=input()
for i in range(n):
    for j in range(len(s)//n):
        if j % 2 == 0:
            print(s[j*n+i], end='')
        else:
            print(s[(j+1)*n-i-1], end='')