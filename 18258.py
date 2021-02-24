import sys
#deque 없이 푸는 법.
n=int(sys.stdin.readline())
fro=0
last=0
que=[]
def Push(n):
    global last
    que.append(n)
    last+=1
def Empty():
    global fro,last
    if fro==last: return True
    return False
def Front():
    global fro
    if Empty(): return -1
    return que[fro]
def Back():
    global last
    if Empty(): return -1
    return que[last-1]
def Size():
    global fro,last
    return last-fro
def Pop():
    global fro
    if Empty(): return -1
    s=que[fro]
    fro+=1
    return s

for _ in range(n):
    msg=list(sys.stdin.readline().split())
    if msg[0]=="push":
        Push(int(msg[1]))
    elif msg[0]=="front":
        print(Front())
    elif msg[0]=="back":
        print(Back())
    elif msg[0]=="size":
        print(Size())
    elif msg[0]=="empty":
        if Empty(): print(1)
        else: print(0)
    elif msg[0]=="pop":
        print(Pop())
        