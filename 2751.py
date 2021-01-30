#그냥 정렬문제다. 힙소트 직접 구현해보자.
#하지만 힙소트로 하면 시간초과가 난다.
#그런데 mergesort로 하면 시간초과가 나지 않는다!!
import sys
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]

        MergeSort(larr)
        MergeSort(rarr)

        i = 0
        j = 0
        k = 0
        while i<len(larr) and j<len(rarr):
            if larr[i] < rarr[j]:
                arr[k] = larr[i]
                i+=1
            else:
                arr[k] = rarr[j]
                j+=1
            k+=1
        while i<len(larr):
            arr[k] = larr[i]
            i+=1
            k+=1
        while j<len(rarr):
            arr[k] = rarr[j]
            j+=1
            k+=1


#main

#input() 보다 sys.stdin.readline()을 써야지 더 빠른 것 같다

nums = int(input())
arr=[]
temp = 0
for i in range(nums):
    arr.append(int(sys.stdin.readline()))
MergeSort(arr)
for i in range(nums):
    print(arr[i])
