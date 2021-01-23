arr = []

for _ in range(9):
    arr.append(int(input()))

num = sum(arr) - 100

for i in range(9):
    for j in range(9):
        if arr[i]+arr[j] == num:
            count = i
            count1 = j
            break


del arr[count]
del arr[count1]

arr.sort()
for i in range(7):
    print(arr[i])

