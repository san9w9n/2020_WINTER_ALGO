import sys
n,m=map(int,sys.stdin.readline().split())
isused=[True]+[False]*n
arr=[0]*m
def func(k):
    if k==m:
        for x in arr: print(x,end=" ")
        print()
        return
    for i in range(1,n+1):
        if not isused[i]:
            arr[k]=i
            isused[i]=True
            func(k+1)
            isused[i]=False
func(0)