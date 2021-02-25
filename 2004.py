import sys

n=int(sys.stdin.readline())
stk=list(map(int,sys.stdin.readline().split()))
tmp=[]
ans=[-1]
tmp.append(stk.pop())
while stk:
    if tmp[-1]>stk[-1]:
        ans.append(tmp[-1])
        tmp.append(stk.pop())
    else:
        tmp.pop()
    if not tmp:
        ans.append(-1)
        tmp.append(stk.pop())
for x in range(len(ans)-1,0,-1):
    print(ans[x],end=" ")
print(ans[0])
