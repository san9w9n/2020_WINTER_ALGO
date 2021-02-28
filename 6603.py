import sys

def bt(used,s,k,arr):
    if len(s)==6:
        print(*s)
        return 
    for i in range(k,len(arr)):
        if not used[i]:
            used[i]=True
            s.append(arr[i])
            bt(used,s,i,arr)
            used[i]=False
            s.pop()
    
while True:
    arr=list(map(int,sys.stdin.readline().split()))
    if arr[0]==0: break
    n=arr[0]
    isused=[False]*len(arr[1:])
    bt(isused,[],0,arr[1:])
    print()