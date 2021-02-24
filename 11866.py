import sys
from collections import deque

n,k=map(int,sys.stdin.readline().split())
que=deque([x for x in range(1,n+1)])
ans=[]
while len(que)>0:
    que.rotate(-(k-1))
    ans.append(que.popleft())

print('<',end="")
print(', '.join(map(str,ans)),end="")
print('>')