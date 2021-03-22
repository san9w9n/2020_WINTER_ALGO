def solution(N, stages):
    answer = []
    
    tried=[-1]+[0]*(N+1)
    fail=[-1]+[0]*(N+1)
    
    for stage in stages:
        for i in range(1,stage+1): tried[i]+=1
        fail[stage]+=1
    
    div=[]
    for i in range(1,N+1):
        if tried[i]: div.append((i,fail[i]/tried[i]))
        else: div.append((i,0))
    
    div.sort(key=lambda x:x[1],reverse=True)
    for i in range(N):
        answer.append(div[i][0])
                        
    return answer