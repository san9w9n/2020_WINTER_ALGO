import sys

n=int(sys.stdin.readline())
answer=[]

def find_vps(s):
    cnt=1
    if(len(s)%2==1): return False
    while cnt:
        if "()" in s:
            if len(s)==2:
                cnt=1
                break
            i=s.index("()")
            s=s[:i]+s[i+2:]
        else:
            cnt=0
            break
    if cnt==1: return True
    elif cnt==0: return False

for _ in range(n):
    s=sys.stdin.readline().strip()
    if find_vps(s): answer.append("YES")
    else: answer.append("NO")

for i in range(n):
    print(answer[i])