import sys
n=int(sys.stdin.readline())
dis=list(map(int,sys.stdin.readline().split()))
oil=list(map(int,sys.stdin.readline().split()))

for i in range(n-2):
    if oil[i]<=oil[i+1]:
        oil[i+1]=oil[i]
    else:
        continue

total=0
for i in range(n-1):
    total+=oil[i]*dis[i]
    
print(total)