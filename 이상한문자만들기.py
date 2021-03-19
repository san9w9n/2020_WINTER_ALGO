def solution(s):
    answer = ''
    idx=0
    for char in s:
        if char==" ":
            answer+=" "
            idx=0
        elif idx%2==0:
            answer+=char.upper()
            idx+=1
        else:
            answer+=char.lower()
            idx+=1

    return answer