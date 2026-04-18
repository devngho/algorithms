_,arr=input(),list(input().split())
a,b,c=arr.count('1'),arr.count('-1'),arr.count('0')

if len(arr)/2 <= c: print('INVALID')
else: print('APPROVED' if a > b else 'REJECTED')