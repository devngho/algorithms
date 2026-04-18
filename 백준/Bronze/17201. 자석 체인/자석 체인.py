n, s=int(input()),input()
ok=True
for i in range(2*n-1):
    if s[i]==s[i+1]:
        ok=False
        break
print('Yes' if ok else 'No')