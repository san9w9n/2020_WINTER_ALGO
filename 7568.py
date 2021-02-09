import sys
n=int(sys.stdin.readline())
rank=[0]*n
arr=[]
for _ in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))


for i in range(n):
    count=1
    for j in range(n):
        if arr[i][0]==arr[j][0] and arr[i][1]==arr[j][1]:
            continue
        elif arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            count+=1
    rank[i]=count

for x in range(n):
    if x==n-1: print(rank[x])
    else: print(rank[x],end=" ")
        