from collections import deque
def solution(s):
    answer = 0
    if len(s)==2 and s[0]==s[1]: return 1
    que=deque(s[1:])
    tmp=deque([s[0]])
    
    while que:
        if not tmp: tmp.append(que.popleft())
        
        if que:
            if que[0]==tmp[-1]:
                que.popleft()
                tmp.pop()
            else:
                tmp.append(que.popleft())
        
    if not tmp: answer=1
        
    return answer