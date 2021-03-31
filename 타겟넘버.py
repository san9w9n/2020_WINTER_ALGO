from collections import deque

def solution(numbers, target):
    answer = 0
    
    que=deque([numbers[0],-numbers[0]])
    for i in range(1,len(numbers)):
        for _ in range(len(que)):
            now=que.popleft()
            que.append(now+numbers[i])
            que.append(now-numbers[i])
    
    answer=que.count(target)
    return answer