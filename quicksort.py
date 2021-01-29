#quick sort 공부. 직접 알고리즘 짜보기
#재귀함수로 짜보자

def quicksort(arr, start, end):
    if start >= end: return #리스트가 하나밖에 남지 않으면 함수 종료
    pivot, i, j = start, start+1, end #pivot을 배열(나눈 것)에 제일 처음 값으로 넣는다
    temp = 0

    while i<=j:
        while i <= end and arr[i] <= arr[pivot]: i+=1 #arr[i] 가 피벗값보다 크면 종료
        while j > start and arr[j] >= arr[pivot]: j-=1
        if i>j: #엇갈린 상태면 키 값과 교체
            temp = arr[j]
            arr[j] = arr[pivot]
            arr[pivot] = temp
        else: #엇갈리지 않으면 i와 j를 교체!
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    quicksort(arr, start, j-1)
    quicksort(arr, j+1, end)

q_arr = list(map(int,input().split()))
quicksort(q_arr,0,len(q_arr)-1)
print(q_arr)
    
        