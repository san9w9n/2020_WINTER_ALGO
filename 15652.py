import sys

n,m=map(int,sys.stdin.readline().split())
arr=[0]*m
isused=[True]+[False]*n

def func(k):
    if k==m:
        print(*arr)
        return
    for i in range(1,n+1):
        if not isused[i]:
            arr[k]=i
            for j in range(i):
                isused[j]=True
            func(k+1)
            for j in range(i+1):
                isused[j]=False
func(0)