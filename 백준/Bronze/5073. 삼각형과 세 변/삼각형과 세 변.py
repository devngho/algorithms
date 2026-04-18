while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    
    if a < c and b < c:
        m,s=c,a+b
    elif a < b and c < b:
        m,s=b,a+c
    else:
        m,s=a,b+c
    
    if not m<s:
        print('Invalid')
    elif a==b and b==c:
        print('Equilateral')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')