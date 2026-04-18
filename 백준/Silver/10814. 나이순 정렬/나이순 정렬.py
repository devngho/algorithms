people = [(lambda x: (int(x[0]), x[1]))(input().split()) for _ in range(int(input()))]
people = sorted(people, key=lambda x: x[0])

print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', people)))