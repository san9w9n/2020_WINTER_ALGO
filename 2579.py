import sys
N=int(sys.stdin.readline())
stair=[]
for _ in range(N):
    stair.append(int(sys.stdin.readline()))
if N==1:
    print(stair[0])
    sys.exit(0)
if N==2:
    print(stair[0]+stair[1])
    sys.exit(0)
if N==3:
    print(max(stair[0]+stair[2],stair[1]+stair[2]))
    sys.exit(0)
dp=[stair[0],stair[0]+stair[1],max(stair[0]+stair[2],stair[1]+stair[2])]
#4번째칸부터 가능
#N=(N-3)까지에 (N-1)+N 더하면 됨 
#N=(N-2)중 최댓값에 마지막칸 더하면 됨
for i in range(3,N):
    dp.append(max(dp[i-2]+stair[i], dp[i-3]+stair[i]+stair[i-1]))
print(dp[-1])




    

