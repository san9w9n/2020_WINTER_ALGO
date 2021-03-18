def solution(n):
    answer = 0
    tri=[]
    while n>=3:
        tri.append(n%3)
        n//=3
    tri.append(n%3)
    
    l=len(tri)
    for i in range(l):
        answer+=tri[i]*(3**(l-i-1))
    
    return answer