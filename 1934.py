import sys

#gcd 사용하면 수행시간이 많이 빨라진다
def gcd(a,b):
    if b==0: return a
    return gcd(b,a%b)

T=int(sys.stdin.readline())
arr=[]
for _ in range(T):
    a,b=map(int,sys.stdin.readline().split())
    arr.append((a*b)//gcd(a,b))

for i in range(T):
    print(arr[i])
