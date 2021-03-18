def solution(n, lost, reserve):
    answer = 0
    
    arr=[-1]+[1]*n
    
    for p in reserve: arr[p]+=1
    for p in lost:
        if arr[p]==2: arr[p]=1
        else: arr[p]=0
        
    for i in range(1,n+1):
        if arr[i]==2 and arr[i-1]==0:
            arr[i]-=1
            arr[i-1]+=1
        elif i!=n and arr[i]==2 and arr[i+1]==0:
            arr[i]-=1
            arr[i+1]+=1
            
    for i in range(1,n+1):
        if arr[i]>0: answer+=1

    return answer