def solution(n):
    answer = ''
    even="수박"
    odd="수"
    if n%2==0:
        answer+=even*(n//2)
    else:
        answer+=even*((n-1)//2)
        answer+=odd
    return answer