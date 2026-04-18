n,m=map(int,input().split())
arr=[list(input()) for _ in range(n)]
students=[]

if n != 1:
    for i in range(m):
        p=False
        for j in range(n):
            if arr[j][i] == 'O' or p:
                p=False
                continue
            
            if j+1 < n and arr[j+1][i] == 'X':
                students.append((2, [i*n+j+1, i*n+j+2]))
                p=True
            else:
                students.append((1, [i*n+j+1]))
else:
    p=False
    for i in range(m):
        if arr[0][i] == 'O' or p:
            p=False
            continue
        
        if i+1 < m and arr[0][i+1] == 'X':
            students.append((2, [i+1, i+2]))
            p=True
        else:
            students.append((1, [i+1]))

print(len(students))
for i in students:
    print(i[0], *i[1])