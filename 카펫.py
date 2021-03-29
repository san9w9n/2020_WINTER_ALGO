def solution(brown, yellow):
    answer = []
    total = brown + yellow
    pair=[(1,total)]
    for i in range(2,int(total**0.5)+1):
        if total%i==0: pair.append((i,total//i))
    
    for e in pair:
        garo=max(e[0],e[1])
        sero=min(e[0],e[1])
        if brown == (2*garo)+(2*(sero-2)) and yellow==total-brown:
            answer.append(garo)
            answer.append(sero)
            
    return answer