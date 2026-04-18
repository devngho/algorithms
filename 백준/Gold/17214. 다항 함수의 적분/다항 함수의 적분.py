def integrate(s):
    if len(s) == 0: return ''

    v = 1
    cur = 0
    if s[0] == '-':
        is_negative = True
        cur += 1
    elif s[0] == '+':
        is_negative = False
        cur += 1
    else:
        is_negative = False
    if s[cur].isdigit():
        v = 0

        while cur < len(s):
            if s[cur].isdigit():
                v *= 10
                v += int(s[cur])
                cur += 1
            else:
                break

    if v == 0: return ''

    if cur == len(s):
        return ('-' if is_negative else '+') + (f'{v}x' if v != 1 else 'x')
    else:
        return ('-' if is_negative else '+') + (f'{v//2}xx' if v != 2 else 'xx')


inp = input()
args = ['']
for i in inp:
    if i != '+' and i != '-':
        args[-1] = args[-1] + i
    else:
        args.append(i)

print((''.join(map(integrate, args)) + '+W').lstrip('+'))