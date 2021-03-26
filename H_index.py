def solution(citations):
    answer = 0
    
    arr=[0]+[0]*10000
    for e in citations: arr[e]+=1
    citations=sorted(list(set(citations)))
    n=max(citations)
    ans=[]
    for i in range(n+1):
        tl,tr=0,0
        for j in range(i,n+1):
            tl+=arr[j]
        for k in range(i):
            tr+=arr[k]
            
        if tl>=i and tr<=i:
            ans.append(i)
            
    answer=max(ans)
    return answer