import sys

n,m=map(int,sys.stdin.readline().split())
arr=[0]*m
isused=[True]+[False]*n
def func(k):
    if k==m:
        for i in range(m-1):
            if arr[i]>arr[i+1]:
                return
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