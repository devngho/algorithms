for _ in range(int(input())):
    a,s=input().split()
    a=int(a)
    print(s[:a-1]+s[a:])