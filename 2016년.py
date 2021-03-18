def solution(a, b):
    answer = ''
    m,d=1,1
    
    day=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    total=0
    for i in range(a): total+=month[i]
    total+=b
    
    d=d%7
    total=total%7
    
    idx=(5+(total-d))%7
    answer+=day[idx]
    return answer