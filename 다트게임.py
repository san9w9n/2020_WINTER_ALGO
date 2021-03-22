def solution(dartResult):
    answer = 0
    
    arr=['']*len(dartResult)
    k=0
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i]=='1' and dartResult[i+1]=='0':
                k+=1
                arr[k]+='10'
            elif dartResult[i]=='0':
                if arr[k]=='10': continue
                else:
                    k+=1
                    arr[k]+='0'
                
            else:
                k+=1
                arr[k]+=dartResult[i]
        elif dartResult[i]=='S': arr[k]+='**1'
        elif dartResult[i]=='D': arr[k]+='**2'
        elif dartResult[i]=='T': arr[k]+='**3'
        elif dartResult[i]=='*':
            if arr[k-1]!="":
                arr[k-1]+='*2'
            arr[k]+='*2'
        elif dartResult[i]=='#':
            arr[k]='-(' + arr[k] + ')'
    print(arr)
    total=[]
    for e in arr:
        if e!="":
            total.append(eval(e))
    
    answer=sum(total)
    
    return answer