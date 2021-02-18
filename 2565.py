import sys
count=[0]+[0]*500
N=int(sys.stdin.readline())
arr=[]
maxi=0
for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    if maxi<=a: maxi=a
    count[a]=b
for i in range(maxi+1):
    if count[i]!=0:
        arr.append([i,count[i]])
dp=[1]*N
for i in range(1,N):
    for j in range(i):
        if arr[i][1]>arr[j][1]:
            if dp[i]<=dp[j]+1:
                dp[i]=dp[j]
                dp[i]+=1
print(N-max(dp))


