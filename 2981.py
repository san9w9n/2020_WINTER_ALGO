import sys

n=int(sys.stdin.readline())
arr=[]
ans=[]
m=0

def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

for i in range(n):
    arr.append(int(sys.stdin.readline()))
    if i==1: m=abs(arr[1]-arr[0])
    m=gcd(abs(arr[i]-arr[i-1]),m)

sqrt=int(m**0.5)
for i in range(2,sqrt+1):
    if m%i==0:
        ans.append(i)
        ans.append(m//i)
ans.append(m)
ans=list(set(ans))
ans.sort()
print(*ans)