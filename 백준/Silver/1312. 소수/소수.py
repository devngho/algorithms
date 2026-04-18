# Baekjoon 1312
# solved.ac Silver 5

A, B, N = map(int, input().split())

for i in range(N):
    A = (A % B) * 10

print(A//B)
