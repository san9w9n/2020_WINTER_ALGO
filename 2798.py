import sys
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
total=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if m>=arr[i]+arr[j]+arr[k]:
                if total<=arr[i]+arr[j]+arr[k]:
                    total=arr[i]+arr[j]+arr[k]
print(total)
