import sys
arr = []
for _ in range(3):
    arr.append(list(map(int,sys.stdin.readline().split())))

if arr[0][0]==arr[1][0]:
    x = arr[2][0]
elif arr[0][0]==arr[2][0]:
    x = arr[1][0]
else:
    x = arr[0][0]


if arr[0][1]==arr[1][1]:
    y = arr[2][1]
elif arr[0][1]==arr[2][1]:
    y = arr[1][1]
else:
    y = arr[0][1]

print("{} {}".format(x,y))