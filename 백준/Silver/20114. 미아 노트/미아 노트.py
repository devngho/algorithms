n,h,w=map(int,input().split())
arr=[list(input()) for _ in range(h)]

for i in range(n):
    char='?'
    for j in range(h):
        for k in range(w*i, w*(i+1)):
            if arr[j][k] != '?':
                char = arr[j][k]
                break
        if char != '?':
            break
    
    print(char, end='')