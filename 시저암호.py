def solution(s, n):
    answer = ''
    low="abcdefghijklmnopqrstuvwxyz"
    up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for char in s:
        if char==" ": answer+=" "
        elif 65<=ord(char)<=90:
            answer+=up[(ord(char)-65+n)%26]
        else: answer+=low[(ord(char)-97+n)%26]
    return answer