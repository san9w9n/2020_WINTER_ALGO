import sys
sys.setrecursionlimit(10000)
T=int(sys.stdin.readline())

def dfs(r,c):
    if 0<=r<n and 0<=c<m:
        if field[r][c]==1:
            field[r][c]=0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        else:
            return
    else: return

for _ in range(T):
    m,n,k=map(int,sys.stdin.readline().split())
    field=[[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        pos=list(map(int,sys.stdin.readline().split()))
        field[pos[1]][pos[0]]=1

    result=0
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                dfs(i,j)
                result+=1
    
    print(result)
