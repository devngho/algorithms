for _ in range(int(input())):
    score = sum(map(lambda x: ord(x)-ord('A')+1, input().replace(' ', '')))
    print('PERFECT LIFE' if score == 100 else score)