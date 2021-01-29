#이 문제는 음수도 없으니까 빠르게 계수정렬로 정렬후에
#더해버리면 된다.
def CountingSort(arr):
    count = [0] * 1001
    new_arr = []
    for i in arr:
        count[i]+=1
    for i in range(1001):
        if count[i] != 0:
            for _ in range(count[i]):
                new_arr.append(i)
    return new_arr

N = int(input())
arr = list(map(int,input().split()))
arr = CountingSort(arr)

total = 0
for i in range(N):
    total += arr[i] * (N-i)

print(total)
    