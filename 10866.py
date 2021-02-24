import sys
from collections import deque

n=int(sys.stdin.readline())
que=deque([])

for _ in range(n):
    msg=list(sys.stdin.readline().split())
    o=msg[0]
    if o=="push_front": que.appendleft(msg[1])
    elif o=="push_back": que.append(msg[1])
    elif o=="pop_front":
        if que: print(que.popleft())
        else: print(-1)
    elif o=="pop_back":
        if que: print(que.pop())
        else: print(-1)
    elif o=="size": print(len(que))
    elif o=="empty":
        if que: print(0)
        else: print(1)
    elif o=="front":
        if que: print(que[0])
        else: print(-1)
    elif o=="back":
        if que: print(que[-1])
        else: print(-1)