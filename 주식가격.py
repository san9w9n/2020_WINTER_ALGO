def solution(prices):
    answer = [0]*len(prices)
    price=[]
    for i in range(len(prices)-1,-1,-1):
        price.append((i,prices[i]))
    sec=0
    stk=[]
    p=price.pop()
    stk.append([p[0],p[1],sec])
    while price:
        if not stk:
            sec+=1
            p=price.pop()
            stk.append([p[0],p[1],sec])
        if stk[-1][1]<=price[-1][1]:
            sec+=1
            p=price.pop()
            stk.append([p[0],p[1],sec])
        elif stk[-1][1]>price[-1][1]:
            s=stk.pop()
            answer[s[0]]=sec+1-s[2]
    for arr in stk:
        answer[arr[0]]=sec-arr[2]
        
    return answer