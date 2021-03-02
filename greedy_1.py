import sys
n=int(sys.stdin.readline())
h=list(map(int,sys.stdin.readline().split()))
h.sort()

group=0
index=0
saram=0
maxi=0
while True:
    if index==n: break
    if maxi<=h[index]: maxi=h[index]
    saram+=1
    if maxi==saram:
        group+=1
        index+=1
        saram=0
    else: index+=1
print(group)