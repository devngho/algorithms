arr={0}
n=int(input())

for i in range(n):
    next_arr=set()
    for j in arr:
        next_arr.add(j+1)
        next_arr.add(j+5)
        next_arr.add(j+10)
        next_arr.add(j+50)
    
    arr = next_arr

print(len(arr))