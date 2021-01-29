#CountingSort, 계수정렬
def CountingSort(arr):
    count = [0] * sum(arr)
    new_arr = []
    for i in arr:
        count[i]+=1
    for i in range(sum(arr)):
        if count[i] != 0:
            for _ in range(count[i]):
                new_arr.append(i)
    return new_arr

arr = list(map(int,input().split()))
arr = CountingSort(arr)
print(arr)