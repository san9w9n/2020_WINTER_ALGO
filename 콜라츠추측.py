def solution(num):
    answer = -1
    if num==1: return 0
    for i in range(1,501):
        if num%2==0: num//=2
        else: num=num*3+1
        
        if num==1:
            answer=i
            return answer
    return answer