for _ in range(int(input())):
    _, a, b = input(), set(map(int, input().split())), set(map(int, input().split()))
    
    print(len(a.intersection(b)))