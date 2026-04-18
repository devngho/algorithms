ulim = list(map(int, input().split()))
startlink = list(map(int, input().split()))

ulim_score = 0
startlink_score = 0
no = True

for i in range(9):
    ulim_score += ulim[i]
    if ulim_score > startlink_score:
        print("Yes")
        no = False
        break
    startlink_score += startlink[i]

if no: print("No")