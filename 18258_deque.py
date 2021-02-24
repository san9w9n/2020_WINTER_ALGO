import sys
from collections import deque
n=int(sys.stdin.readline())
que=deque()
#deque 를 하면 시간이 빠르다!

def Empty():
    if len(que)==0: return True
    return False

for _ in range(n):
    msg=list(sys.stdin.readline().split())
    if msg[0]=="push": que.append(msg[1])
    elif msg[0]=="pop":
        if not Empty(): print(que.popleft())
        else: print(-1)
    elif msg[0]=="size": print(len(que))
    elif msg[0]=="empty":
        if not Empty(): print(0)
        else: print(1)
    elif msg[0]=="front":
        if not Empty(): print(que[0])
        else: print(-1)
    elif msg[0]=="back":
        if not Empty(): print(que[-1])
        else: print(-1)