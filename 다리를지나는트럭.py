from collections import deque

def total(arr):
    n=0
    for e in arr:
        n+=e[1]
    return n


def solution(bridge_length, weight, truck_weights):
    answer = 0
    wait=deque(truck_weights)
    going=deque([])
    sec=1
    going.append((0,wait.popleft()))
    while wait or going:
        while going:
            if sec-going[0][0]==bridge_length: going.popleft()
            else: break
                
        if wait:
            if total(going)+wait[0] <= weight:
                going.append((sec,wait.popleft()))
        
        sec+=1
        
    return sec