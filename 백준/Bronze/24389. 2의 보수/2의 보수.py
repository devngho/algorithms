n=int(input())
print(bin(n^(-n&0xffffffff)).count('1'))