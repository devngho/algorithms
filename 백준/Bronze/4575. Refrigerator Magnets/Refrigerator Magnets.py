while True:
    inp=input()
    if inp == 'END':
        break
    chars = set()
    ok=True
    
    for i in inp:
        if i == ' ':
            continue
        
        if i in chars:
            ok=False
            break
        else:
            chars.add(i)
    
    if ok:
        print(inp)