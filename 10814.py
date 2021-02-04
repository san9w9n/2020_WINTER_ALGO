import sys
def merge(arr):
    if len(arr)>1:
        mid = len(arr)//2
        larr = arr[:mid]
        rarr = arr[mid:]

        merge(larr)
        merge(rarr)

        i,j,k = 0,0,0
        while i<len(larr) and j<len(rarr):
            if larr[i][0] < rarr[j][0]:
                arr[k] = larr[i]
                i+=1
            elif larr[i][0] > rarr[j][0]:
                arr[k] = rarr[j]
                j+=1
            elif larr[i][0] == rarr[j][0] and larr[i][2] < rarr[j][2]:
                arr[k] = larr[i]
                i+=1
            elif larr[i][0] == rarr[j][0] and larr[i][2] >= rarr[j][2]:
                arr[k] = rarr[j]
                j+=1
            k+=1

        while i<len(larr):
            arr[k]=larr[i]
            i+=1
            k+=1
        while j<len(rarr):
            arr[k]=rarr[j]
            j+=1
            k+=1
            

N = int(sys.stdin.readline())
client = []
for i in range(N):
    arr = list(map(str,sys.stdin.readline().split()))
    client.append([int(arr[0]),arr[1],i])

merge(client)
for i in range(N):
    print("{} {}".format(client[i][0],client[i][1]))



