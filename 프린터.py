from collections import deque

def solution(priorities, location):
    answer = 1
    if len(priorities)==1: return 1
    que=deque([])
    rev=deque(sorted(priorities,reverse=True))
    for i in range(len(priorities)):
        que.append((i,priorities[i]))
    if que[0][0]==location and rev[0]==que[0][1]: return 1
    while True:
        
        if que[0][1]==rev[0]:
            answer+=1
            que.popleft()
            rev.popleft()
        else:
            que.rotate(-1)
            
        if que[0][0]==location and rev[0]==que[0][1]: break
        
    return answer