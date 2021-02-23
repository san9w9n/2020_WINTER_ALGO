import sys

n=int(sys.stdin.readline())
stk=[x for x in range(n,0,-1)]
temp=[]
ans=[]

def push():
    temp.append(stk.pop())
    ans.append("+")

def pop():
    temp.pop()
    ans.append("-")

for _ in range(n):
    k=int(sys.stdin.readline())

    if len(stk)>0 and k>=stk[-1]:
        while stk[-1]!=k:
            push()
        push()
        pop()
    else:
        if len(temp)>0 and temp[-1]==k:
            pop()
        else:
            ans.append(-1)

if -1 in ans:
    print("NO")
else:
    for s in ans:
        print(s)

