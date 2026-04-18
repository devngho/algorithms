for _ in range(int(input())):
    a, op, b, _, r = input().split()
    a, b, r = int(a), int(b), int(r)
    res=0
    match op:
        case '+':
            res=a+b
        case '-':
            res=a-b
        case '*':
            res=a*b
        case '/':
            res=a//b
    if r == res: print('correct')
    else: print('wrong answer')