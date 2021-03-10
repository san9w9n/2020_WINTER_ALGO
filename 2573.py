import sys
sys.setrecursionlimit(100000)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def melt():
    copy = [item[:] for item in ice]
    for r in range(1,n-1):
        for c in range(1,m-1):
            if copy[r][c]>0:
                cnt=0
                for i in range(4):
                    x,y=r+dx[i],c+dy[i]
                    if copy[x][y]==0:
                        cnt+=1
                ice[r][c]=max(copy[r][c]-cnt,0)

def dfs(r,c):
    visited[r][c]=True

    for i in range(4):
        x,y=r+dx[i],c+dy[i]
        if 1<=x<n-1 and 1<=y<m-1:
            if ice[x][y]>0 and not visited[x][y]:
                dfs(x,y)


n,m=map(int,sys.stdin.readline().split())
ice=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited=[[False for _ in range(m)] for _ in range(n)]
year=0


while True:
    for i in range(n):
        for j in range(m):
            visited[i][j]=False
    result=False
    cnt=0

    for i in range(1,n-1):
        for j in range(1,m-1):
            if ice[i][j]>0 and not visited[i][j]:
                cnt+=1
                if cnt==2:
                    result=True
                    break
                dfs(i,j)

    if result: break
    if cnt==0:
        year=0
        break

    melt()
    year+=1

print(year)