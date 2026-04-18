def solve(A, B):
    A = set(map(int, A.split()))
    B = set(map(int, B.split()))
    diff = sorted(A-B)
    print(len(diff))
    for i in diff:
        print(i, end=' ')
    return 0


input()
A = input()
B = input()
solve(A, B)