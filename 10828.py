import sys
arr=[]
def push(n):
    arr.append(n)
def pop():
    if len(arr)==0:
        print(-1)
    else: print(arr.pop(-1))
def size():
    print(len(arr))
def empty():
    if len(arr)==0:
        print(1)
    else: print(0)
def top():
    if len(arr)==0:
        print(-1)
    else: print(arr[-1])


n=int(sys.stdin.readline())
for _ in range(n):
    msg=list(map(str,sys.stdin.readline().split()))
    if len(msg)==2:
        push(int(msg[1]))
    else:
        if msg[0]=="top": top()
        elif msg[0]=="size": size()
        elif msg[0]=="empty": empty()
        elif msg[0]=="pop": pop()