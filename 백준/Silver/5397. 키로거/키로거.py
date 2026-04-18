for _ in range(int(input())):
    # doubly linked list
    root = ['', None, None] # value, back, front
    cursor = root
    for i in input():
        match i:
            case '<':
                if cursor[1] != None:
                    cursor = cursor[1]
            case '>':
                if cursor[2] != None:
                    cursor = cursor[2]
            case '-':
                p, n = cursor[1], cursor[2]
                if p != None:
                    p[2]=n
                    cursor=p
                    if n != None:
                        n[1]=p
            case _:
                p, n = cursor, cursor[2]
                cursor = [i, cursor, cursor[2]]
                if p != None:
                    p[2]=cursor
                if n != None:
                    n[1]=cursor
    cursor=root
    while cursor[2] != None:
        print(cursor[0], end='')
        cursor=cursor[2]
    print(cursor[0], end='')
     
    print()