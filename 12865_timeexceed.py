import sys

n,k=map(int,sys.stdin.readline().split())
s=[]
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))
ans=0
def dp(d,w,v):
    global k,ans
    if d==0: 
        if w+s[0][0]<=k:
            ans=max(v+s[0][1],ans)
            return
        else:
            ans=max(v,ans)
            return
    
    if w+s[d][0]<=k:
        dp(d-1,w+s[d][0],v+s[d][1])
    dp(d-1,w,v)
    

dp(n-1,0,0)
print(ans)