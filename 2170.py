import sys

n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(tuple(map(int,sys.stdin.readline().split())))
arr.sort()

total=0

x=arr[0][0]
y=arr[0][1]
for i in range(1,n):
    if arr[i][0]<=y:
        y=max(y,arr[i][1])
    else:
        total+=y-x
        x=arr[i][0]
        y=arr[i][1]
total+=y-x
print(total)
