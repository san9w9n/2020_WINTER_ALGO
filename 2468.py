import sys, copy
sys.setrecursionlimit(12000)

n=int(sys.stdin.readline())
field=[]
for _ in range(n): field.append(list(map(int,sys.stdin.readline().split())))

def dfs(r,c,h):
    if 0<=r<n and 0<=c<n:
        if field[r][c]>h:
            field[r][c]=-1
            dfs(r+1,c,h)
            dfs(r-1,c,h)
            dfs(r,c+1,h)
            dfs(r,c-1,h)
            return
        else:
            return
    else: return

temp=copy.deepcopy(field)
maxi=0
for h in range(101):
    result=0
    for i in range(n):
        for j in range(n):
            if field[i][j]>h:
                dfs(i,j,h)
                result+=1
    if result==0: break
    field=copy.deepcopy(temp)
    maxi=max(result,maxi)
print(maxi)