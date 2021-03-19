def solution(nums):
    answer = 1
    select=len(nums)//2
    nums=list(set(nums))
    now=nums[0]
    
    if select!=answer:
        for i in nums[1:]:
            if now!=i:
                answer+=1
                now=i
                if select==answer:
                    break
                
    return answer