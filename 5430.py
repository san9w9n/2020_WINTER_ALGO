import sys
from collections import deque

N=int(sys.stdin.readline())
for _ in range(N):
    p=sys.stdin.readline().rstrip()
    n=int(sys.stdin.readline())
    que = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    rev=1
    error=0
    for s in p:
        if s=="R": rev*=-1
        elif s=="D" and len(que)==0:
            error=1
            break
        elif s=="D" and len(que)==1 and que[0]=="":
            error=1
            break
        if rev==1 and s=="D":
            que.popleft()
        elif rev==-1 and s=="D":
            que.pop()
    if error==1: print("error")
    else:   
        if rev==1:
            print('[' + ','.join(que) + ']')
        elif rev==-1:
            print('[' + ','.join(reversed(que)) + ']')



        