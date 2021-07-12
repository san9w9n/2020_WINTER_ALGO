import sys
input = sys.stdin.readline

N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

lcross = [False] * (2*N)
rcross = [False] * (2*N)

def erase(r,c):
    lcross[r-c+N-1] = True
    rcross[r+c] = True
def recover(r,c):
    lcross[r-c+N-1] = False
    rcross[r+c] = False

maxi = [0,0]
def dfs(r,c,cnt,bw):
    global maxi
    maxi[bw] = max(maxi[bw], cnt)
    if c>=N:
        r+=1
        if bw==0: c = r%2
        else: c = 1 - (r%2)
    if r>=N: return
    if field[r][c]==1 and not lcross[r-c+N-1] and not rcross[r+c]:
        erase(r,c)
        dfs(r, c+2, cnt+1, bw)
        recover(r,c)
    dfs(r,c+2,cnt,bw)

dfs(0,0,0,0)
dfs(0,1,0,1)
print(sum(maxi))