import sys
n,m=map(int,sys.stdin.readline().split())
arr =[0]*m

def func(k):
    if m==k:
        print(*arr)
        return
    for i in range(1,n+1):
        arr[k]=i
        func(k+1)
func(0)