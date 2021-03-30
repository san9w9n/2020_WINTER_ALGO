def binary(n):
    cnt=0
    while n>=2:
        if n%2==1: cnt+=1
        n//=2
    if n==1: cnt+=1
    return cnt

def solution(n):
    answer = 0
    
    one=binary(n)
    print(binary(23))
    for i in range(n+1,1000001):
        if one==binary(i):
            answer=i
            break
    return answer