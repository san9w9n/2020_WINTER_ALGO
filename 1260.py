import sys
from collections import deque

n,m,v=map(int,sys.stdin.readline().split())
data=[[] + [] for _ in range(n+1)]
for _ in range(m):
    line=list(map(int,sys.stdin.readline().split()))
    data[line[0]].append(line[1])
    data[line[1]].append(line[0])
for l in data: l.sort()

visited=[True]+[False]*n
dfs_ans=[]
def dfs(k):
    visited[k] = True
    dfs_ans.append(k)
    for i in data[k]:
        if not visited[i]:
            dfs(i)

visited2=[True]+[False]*n
bfs_ans=[]
def bfs(k):
    que=deque([k])
    visited2[k] = True
    while que:
        v = que.popleft()
        bfs_ans.append(v)
        for i in data[v]:
            if not visited2[i]:
                que.append(i)
                visited2[i]=True

dfs(v)
bfs(v)
print(*dfs_ans)
print(*bfs_ans)