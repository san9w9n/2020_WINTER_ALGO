#알고리즘 공부 방법 변경.
#탐색 -> 그리디 -> 동적 프로그래밍 순으로 공부하고
#각 분야에 해당하는 백준 문제 풀고, 기출문제 푼다.

#Selection Sort, 선택정렬
#O(n^2)
def Selection():
    pos = 0
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        mini = 9999
        for j in range(len(arr)):
            if j>=i and mini > arr[j]:
                pos = j
                mini = arr[j]
        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp
    print(arr)
    
    
#Bubble Sort, 버블정렬
#O(n^2)
def Bubble():
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i<=j and arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    print(arr)

#Insertion Sort, 삽입정렬
def Insertion():
    arr = list(map(int,input().split()))
    for i in range(len(arr)-1):
        j=i
        while(j>=0 and arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            j-=1
    print(arr)