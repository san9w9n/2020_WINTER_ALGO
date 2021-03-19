def solution(n):
    answer = 0
    if n==0: return 0
    
    arr=set()
    arr.add(1)
    arr.add(n)
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            arr.add(i)
            arr.add(n//i)
    answer=sum(list(arr))
    return answer