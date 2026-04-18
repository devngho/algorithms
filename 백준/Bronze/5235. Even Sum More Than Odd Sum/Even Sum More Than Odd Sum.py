for _ in range(int(input())):
    arr=list(map(int, input().split()))[1:]
    even=sum(filter(lambda x: x%2==0, arr))
    odd=sum(filter(lambda x: x%2==1, arr))
    if even == odd:
        print("TIE")
    elif even > odd:
        print("EVEN")
    else:
        print("ODD")