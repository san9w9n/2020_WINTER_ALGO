import sys, copy
sys.setrecursionlimit(12000)

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(r,c,now):
    pic[r][c]=0
    for i in range(4):
        x,y=r+dx[i],c+dy[i]
        if 0<=x<n and 0<=y<n and pic[x][y]!=0 and now==pic[x][y]:
            dfs(x,y,now)

def r_dfs(r,c,now):
    redpic[r][c]=0
    for i in range(4):
        x,y=r+dx[i],c+dy[i]
        if 0<=x<n and 0<=y<n and redpic[x][y]!=0 and now==redpic[x][y]:
            r_dfs(x,y,now)


n=int(sys.stdin.readline())
pic=[]
for _ in range(n):
    pic.append(list(sys.stdin.readline().rstrip()))
redpic=copy.deepcopy(pic)

for i in range(n):
    for j in range(n):
        if redpic[i][j]=="G":
            redpic[i][j]="R"

ans1=0
ans2=0
for i in range(n):
    for j in range(n):
        if pic[i][j]!=0:
            dfs(i,j,pic[i][j])
            ans1+=1
        if redpic[i][j]!=0:
            r_dfs(i,j,redpic[i][j])
            ans2+=1
print(f'{ans1} {ans2}')
            
