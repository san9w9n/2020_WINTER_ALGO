def solution(answers):
    answer = []
    n=len(answers)
    one=[x for _ in range(1 + n//5) for x in range(1,6)]
    two=[x for _ in range(1 + n//8) for x in [2,1,2,3,2,4,2,5]]
    three=[x for _ in range(1+ n//10) for x in [3,3,1,1,2,2,4,4,5,5]]
    
    ans1,ans2,ans3=0,0,0
    for i in range(n):
        if one[i]==answers[i]: ans1+=1
        if two[i]==answers[i]: ans2+=1
        if three[i]==answers[i]: ans3+=1
    
    maximum = max(ans1,ans2,ans3)        
    if ans1==maximum: answer.append(1)
    if ans2==maximum: answer.append(2)
    if ans3==maximum: answer.append(3)
    return answer