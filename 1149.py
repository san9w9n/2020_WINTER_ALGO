import sys
N=int(sys.stdin.readline())
cost=[]
for _ in range(N):
    cost.append(list(map(int,sys.stdin.readline().split())))

for i in range(1,N):
    cost[i][0]=min(cost[i-1][1],cost[i-1][2]) + cost[i][0]
    cost[i][1]=min(cost[i-1][0],cost[i-1][2]) + cost[i][1]
    cost[i][2]=min(cost[i-1][0],cost[i-1][1]) + cost[i][2]
print(min(cost[N-1][0],cost[N-1][1],cost[N-1][2]))