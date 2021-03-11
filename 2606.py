import sys
from collections import deque
com=int(sys.stdin.readline())
n=int(sys.stdin.readline())

arr=[[] for x in range(com+1)]
for _ in range(n):
    line=list(map(int,sys.stdin.readline().split()))
    arr[line[0]].append(line[1])
    arr[line[1]].append(line[0])

used=[False for _ in range(com+1)]
visited=deque([])

cnt=0
def bfs(k):
    global cnt
    if not used[k]:
        cnt+=1
        used[k]=True
        visited.append(k)

    v=visited.popleft()

    for i in arr[v]:
        if not used[i]:
            bfs(i)

bfs(1)
print(cnt-1)


