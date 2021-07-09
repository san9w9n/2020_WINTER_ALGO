import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

T = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y,N,M):
    global field

    field[x][y] = 0
    for d in range(4):
        r = x + dx[d]
        c = y + dy[d]
        if 0<=r<N and 0<=c<M:
            if field[r][c] == 1:
                dfs(r,c,N,M)


for _ in range(T):
    N, M, K = map(int, input().split())
    record = []
    field = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        record.append((x,y))
        field[x][y] = 1

    ans = 0
    for x, y in record:
        if field[x][y] == 1: 
            dfs(x, y, N, M)
            ans+=1

    print(ans)
    