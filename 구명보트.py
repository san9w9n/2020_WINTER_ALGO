from collections import deque

def solution(people, limit):
    answer = 0
    que=deque(sorted(people))
    
    while que:
        if len(que)>=2 and que[0]+que[-1]<=limit:
            que.popleft()
            que.pop()
            answer+=1
        elif len(que)>=2 and que[0]+que[-1]>limit:
            que.pop()
            answer+=1
        else:
            que.popleft()
            answer+=1
    
    
    return answer