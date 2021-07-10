import sys
input = sys.stdin.readline

R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]

used = [False] * 26

maxi = 0

dx = [0,1,0,-1]
dy = [1,0,-1,0]
def dfs(x,y,cnt):
    global maxi, used
    maxi = max(cnt, maxi)
    for i in range(4):
        r, c = x+dx[i], y+dy[i]
        if 0<=r<R and 0<=c<C and not used[ord(field[r][c])-65]:
            order = ord(field[r][c])-65
            used[order] = True
            dfs(r,c,cnt+1)
            used[order] = False

used[ord(field[0][0])-65] = True
dfs(0,0,1)
print(maxi)