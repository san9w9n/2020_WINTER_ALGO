def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=B[i]*A[i]

    return answer