import sys
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
if n==1:
    print(arr[0])
    sys.exit(0)
if n==2:
    print(arr[0]+arr[1])
    sys.exit(0)
if n==3:
    print(max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2]))
dp=[arr[0],arr[0]+arr[1],max(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])] + [0]*(n-3)

for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])

print(dp[-1])