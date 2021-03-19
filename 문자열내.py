def solution(s):
    answer = False
    
    s=s.lower()
    p=s.count("p")
    y=s.count("y")

    if p==y: answer=True
    return answer