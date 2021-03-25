from collections import deque
def solution(progresses, speeds):
    answer = []
    que=deque([])
    for i in range(len(progresses)):
        div=(100-progresses[i])//speeds[i]
        rem=(100-progresses[i])%speeds[i]
        if rem==0: que.append(div)
        else: que.append(div+1)

    now=que.popleft()
    count=1
    while que:
        if now>=que[0]:
            count+=1
            que.popleft()
        else:
            now=que.popleft()
            answer.append(count)
            count=1
    answer.append(count)
            
        
    return answer