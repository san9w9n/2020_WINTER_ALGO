import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
plus=[1]*n
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            if plus[i]<=plus[j]+1:
                plus[i]=plus[j]+1
minus=plus
for i in range(1,n):
    for j in range(i):
        if arr[i]<arr[j]:
            if minus[i]<=minus[j]+1:
                minus[i]=minus[j]+1
print(max(minus))