import sys
T=int(sys.stdin.readline())
for _ in range(T):
    n=int(sys.stdin.readline())
    arr=[]
    for _ in range(n):
        x,y=map(int,sys.stdin.readline().split())
        arr.append((x,y))
    arr.sort()
    x,y=arr[0][0],arr[0][1]

    ans=1
    for i in range(1,n):
        if y > arr[i][1]:
            ans+=1
            x,y=arr[i][0],arr[i][1]
    
    print(ans)
