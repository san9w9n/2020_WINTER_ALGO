def solution(arr, divisor):
    answer = []
    for e in arr:
        if e%divisor==0:
            answer.append(e)
    if answer: answer.sort()
    else: answer.append(-1)
    return answer