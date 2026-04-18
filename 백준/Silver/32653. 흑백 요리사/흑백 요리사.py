def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm_many(arr):
    while len(arr) != 1:
        a, b = arr[-1], arr[-2]
        del arr[-1]
        del arr[-1]
        
        arr.append(a*b//gcd(a, b))
    
    return arr[0]

_, arr = input(), list(map(int, input().split()))

print(lcm_many(arr)*2)