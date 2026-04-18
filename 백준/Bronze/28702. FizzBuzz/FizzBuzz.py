inp = [input() for _ in range(3)]
last_pos = 0

for i, v in enumerate(inp):
    if v != 'FizzBuzz' and v != 'Fizz' and v != 'Buzz':
        last_pos = int(v) - (i-3)

if last_pos % 15 == 0:
    print('FizzBuzz')
elif last_pos % 3 == 0:
    print('Fizz')
elif last_pos % 5 == 0:
    print('Buzz')
else:
    print(last_pos)