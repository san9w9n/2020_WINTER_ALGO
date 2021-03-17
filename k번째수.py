import copy

def check(arr,command):
    i,j,k=command[0],command[1],command[2]
    temp = copy.deepcopy(arr[i-1:j])
    temp.sort()
    return temp[k-1]

def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(check(array,c))
    return answer