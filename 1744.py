import sys

N=int(sys.stdin.readline())
minus=[]
plus=[]
ans=0
for _ in range(N):
    num=int(sys.stdin.readline())
    if num<=0: minus.append(num)
    elif num==1: ans+=1
    elif num>1: plus.append(num)
minus.sort()
plus.sort(reverse=True)

for i in range(0,len(minus),2):
    if i+1 < len(minus):
        ans+=minus[i]*minus[i+1]
    else: ans+=minus[i]
    
for i in range(0,len(plus),2):
    if i+1 < len(plus):
        ans+=plus[i]*plus[i+1]
    else:
        ans+=plus[i]

print(ans)