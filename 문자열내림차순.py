def solution(s):
    answer = ''
    answer=''.join(map(str,sorted(s,reverse=True)))
    return answer