#MergeSort, 병합정렬
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]

        MergeSort(larr)
        MergeSort(rarr)
        i=0
        j=0
        k=0
        while i < len(larr) and j < len(rarr):
            if larr[i] < rarr[j]:
                arr[k] = larr[i]
                i+=1
            else:
                arr[k] = rarr[j]
                j+=1
            k+=1
        while i < len(larr):
            arr[k]=larr[i]
            i+=1
            k+=1
        while j < len(rarr):
            arr[k]=rarr[j]
            j+=1
            k+=1
    print("Merging ",arr)

array = list(map(int,input().split()))
MergeSort(array)
print(array)

        

