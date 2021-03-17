def solution(numbers):
    answer = []
    dp = [0]*201
    n=len(numbers)
    for i in range(n-1):
        for j in range(i+1,n):
            if dp[numbers[i]+numbers[j]]==0: dp[numbers[i]+numbers[j]]+=1
                
    for i in range(len(dp)):
        if dp[i]!=0: answer.append(i)
    return answer