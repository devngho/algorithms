n,arr=int(input()),list(map(int,input().split()))

def is_prime(n: int) -> bool:
    for i in range(2, round(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if n == 2 and ((arr[0] == 1 and is_prime(arr[1])) or (arr[1] == 1 and is_prime(arr[0]))):
    print('NO')
else:
    print('YES')
    print(2)
    if arr[0] == 1 and is_prime(arr[1]):
        print(arr[1], arr[2])
    elif arr[1] == 1 and is_prime(arr[0]):
        print(arr[0], arr[2])
    else:
        print(arr[0], arr[1])