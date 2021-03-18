def solution(arr):
    answer = []
    now=arr[0]
    answer.append(now)
    for e in arr[1:]:
        if now!=e:
            now=e
            answer.append(now)
    return answer