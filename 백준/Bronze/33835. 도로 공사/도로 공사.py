import math
arr=[tuple(map(int,input().split())) for _ in range(int(input()))]
print(math.sqrt((arr[0][0]-arr[-1][0])**2+(arr[0][1]-arr[-1][1])**2))