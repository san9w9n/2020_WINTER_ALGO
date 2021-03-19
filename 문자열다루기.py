def solution(s):
    answer = False
    if len(s)==6 or len(s)==4:
        if s.isdecimal(): answer=True
    return answer