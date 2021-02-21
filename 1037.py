import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
if n%2==1:
    print(arr[len(arr)//2]**2)
else:
    print(arr[0]*arr[-1])