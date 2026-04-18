def solve(x):
    if list(x) == list(reversed(x)):
        return 'yes'
    return 'no'


inp = []

while True:
    inp_ = input()
    if inp_ == "0":
        break
    inp.append(inp_)

res = [solve(i) for i in inp]
print('\n'.join(res))
