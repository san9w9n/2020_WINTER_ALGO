import sys
n=int(sys.stdin.readline())
apart=[]
for _ in range(n): apart.append(list(sys.stdin.readline().rstrip()))


#dfs 함수
count,maxi=0,0
def dfs(r,c):
    global count,maxi
    if 0<=r<n and 0<=c<n:
        if apart[r][c]=='1':
            apart[r][c]='0'        
            count+=1
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return count
        elif apart[r][c]=='0':
            return
    else:
        return

ans=[]
for i in range(n):
    for j in range(n):
        if apart[i][j]=='1':
            ans.append(dfs(i,j))
            count=0
ans.sort()
print(len(ans))
for i in ans:
    print(i)
