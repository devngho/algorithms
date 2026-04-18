w=[13,7,5,3,3,2]
inp=lambda: sum([i*j for i, j in zip(w, map(int, input().split()))])
a,b=inp(), inp()+1.5
print("cocjr0208" if a > b else "ekwoo")