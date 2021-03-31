def solution(s):
    answer = []
    string=''
    for c in s:
        if c.isdigit() or c==',': string+=c
    arr=list(string.split(','))
    
    re_arr=list(set(arr))
    
    dap=[]
    for e in re_arr:
        dap.append((int(e),arr.count(e)))
    
    dap.sort(key=lambda x:x[1], reverse=True)
    
    for e in dap:
        answer.append(e[0])
    
    
    return answer