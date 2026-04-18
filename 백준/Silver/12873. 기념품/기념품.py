n=int(input())

if n==1:
    print(1)
else:
    arr=list(range(1, n+1))
    pos=0
    
    for i in range(1, n):
        pos += i**3-1
        pos %= n-i+1
        
        del[arr[pos]]
    
    print(arr[0])