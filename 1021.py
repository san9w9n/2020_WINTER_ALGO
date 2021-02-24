import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
k=list(map(int,sys.stdin.readline().split()))
que=deque([x for x in range(1,n+1)])

cnt=0
for i in range(m):
    a=que.index(k[i])
    if a<=len(que)//2:
        que.rotate(-a)
        cnt+=a
    elif a>len(que)//2:
        que.rotate(len(que)-a)
        cnt+=len(que)-a
    que.popleft()
    

print(cnt)


