for _ in range(int(input())):
    inp=int(input())
    
    q=inp//25
    inp%=25
    
    d=inp//10
    inp%=10
    
    n=inp//5
    inp%=5
    
    print(q, d, n, inp)