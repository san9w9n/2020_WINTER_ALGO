import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N, M, K = map(int, input().split())
field = [[1 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    lx, ly, rx, ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            field[y][x] = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]
maxi = 0
def dfs(x,y, ans):
    global maxi
    field[x][y] = 0
    maxi+=1
    for d in range(4):
        r, c = x+dx[d], y+dy[d]
        if 0<=r<N and 0<=c<M and field[r][c]==1:
            field[r][c] = 0
            dfs(r,c, ans+1)
    return maxi

answer = []
for i in range(N):
    for j in range(M):
        if field[i][j] == 1: 
            answer.append(dfs(i,j,0))
            maxi = 0
answer.sort()
print(len(answer))
print(*answer)