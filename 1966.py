import sys
from collections import deque

N=int(sys.stdin.readline())
for _ in range(N):
    n,m=map(int,sys.stdin.readline().split())
    index=deque([x for x in range(n)])
    imp=deque(list(map(int,sys.stdin.readline().split())))
    k=index[m]
    cnt=0
    while True:
        maxi=max(imp)
        while True:
            if imp[0]==maxi: break
            imp.rotate(-1)
            index.rotate(-1)
        imp.popleft()
        cnt+=1
        if index[0]==k: break
        index.popleft()
    print(cnt)
        


