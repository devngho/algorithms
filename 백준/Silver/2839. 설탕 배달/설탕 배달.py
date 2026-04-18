x=int(input())
f=x//5
while ((x-f*5)%3)!=0:
    f-=1
    if f<0:
        print(f)
        exit()
print(f+(x-f*5)//3)