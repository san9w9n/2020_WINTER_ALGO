import sys
#15650_1 보다 훨씬 빠른 속도.
n,m=map(int,sys.stdin.readline().split())
arr=[0]*m
isused=[True]+[False]*n
def func(k):
    if k==m:
        for x in arr: print(x,end=" ")
        print()
        return
    for i in range(1,n+1):
        if not isused[i]:
            arr[k]=i
            for j in range(i+1):
                isused[j]=True
            func(k+1)
            for j in range(i+1):
                isused[j]=False
func(0)