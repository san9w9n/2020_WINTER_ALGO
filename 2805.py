import sys
n,m=map(int,sys.stdin.readline().split())
tree=list(map(int,sys.stdin.readline().split()))

start,end=0,max(tree)
ans=0
while start<=end:
    mid=(start+end)//2

    mess=0
    for t in tree:
        if t>mid: mess+=t-mid
    if mess>=m:
        ans=mid
        start=mid+1
    else: end=mid-1
print(ans)
            