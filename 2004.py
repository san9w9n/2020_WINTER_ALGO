import sys
n,m=map(int,sys.stdin.readline().split())
k=n-m
def div(n,d):
    cnt=0
    while True:
        cnt+=n//d
        n//=d
        if n==0: break
    return cnt
f=div(n,5)-div(m,5)-div(k,5)
t=div(n,2)-div(m,2)-div(k,2)
print(min(f,t))