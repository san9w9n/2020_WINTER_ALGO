def music(minute,s):
    i=0
    j=0
    string=""
    while i<minute:
        j%=len(s)
        if s[j]=="#": string+="#"
        else:
            string+=s[j]
            i+=1
        j+=1
        if i==minute and s[j%len(s)]=="#": string+="#"
        
    return string

def t(at,to):
    at_hour,at_minute=map(int,at.split(":"))
    to_hour,to_minute=map(int,to.split(":"))
    
    
    if to_minute<at_minute:
        to_hour-=1
        to_minute+=60
    
    hour = to_hour - at_hour
    minute = to_minute - at_minute
    return hour*60 + minute


def solution(m, musicinfos):
    answer = ''
    arr=[]
    for s in musicinfos:
        at,to,name,dorae=map(str,s.split(','))
        minute=t(at,to)
        song=music(minute,dorae)
        
        there=song.count(m)
        are=song.count(m+"#")
        
        if there>0 and there-are>0:
            arr.append((minute,name))
    
    if arr:
        arr.sort(key=lambda x:x[0], reverse=True)
        answer+=arr[0][1]
    
    else: answer+="(None)"
    
    return answer