n = int(input())

if n % 2 == 1:
    print('*' * n)
    mid = (n - 1) // 2
    for i in range(mid+1, 0, -1):
        if i == mid + 1:
            print(f"{' ' * (i - 1)}*")
        else:
            print(f"{' ' * (i - 1)}*{' ' * (n-2*i)}*")
else:
    print('I LOVE CBNU')