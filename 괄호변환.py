def isValid(s):
    add=0
    if s=="": return "", ""
    if s[0]=="(": add+=1
    else: add-=1
    idx=1
        
    for c in s[1:]:
        if c=="(": add+=1
        else: add-=1
        idx+=1
            
        if add==0: return s[:idx], s[idx:]
    return s[:idx], s[idx:]

def isRight(s):
    while s.count("()")>0:
        idx=s.index("()")
        s= s[:idx] + s[idx+2:]
        
    if s=="": return True
    else: return False


def solution(p):
    if p=="": return ""
    u,v=isValid(p)
    if isRight(u):
        u+=solution(v)
        return u
    else:
        val="("
        val+=solution(v)
        val+=")"
        tmp=[]
        
        for c in u[1:-1]:
            if c=="(": tmp.append(")")
            else: tmp.append("(")
        val+=''.join(map(str,tmp))
        return val