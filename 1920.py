import sys

N=int(sys.stdin.readline())
a=sorted(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
f=list(map(int,sys.stdin.readline().split()))

def bianry(comp,start,end):
    if start>end: return 0
    mid=(start+end)//2
    if a[mid]==comp: return 1
    elif a[mid]<comp:
        return bianry(comp,mid+1,end)
    else: return bianry(comp,start,mid-1)

for c in f:
    print(bianry(c,0,N-1))