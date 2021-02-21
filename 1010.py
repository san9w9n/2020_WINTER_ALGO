import sys
def C(n,k):
    up=1
    down=1
    for i in range(n,n-k,-1): up*=i
    for i in range(k,0,-1): down*=i
    return up//down

N=int(sys.stdin.readline())
for _ in range(N):
    k,n=map(int,sys.stdin.readline().split())
    print(C(n,k))