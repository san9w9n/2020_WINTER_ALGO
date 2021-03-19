def solution(a, b):
    answer = 0
    i=0
    while i<=len(a)-1:
        answer+=a[i]*b[i]
        i+=1
    return answer