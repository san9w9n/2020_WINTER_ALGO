import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

maxi = 0
arr.sort()
for i in range(n):
    k = (n-i) * arr[i]
    if maxi <= k: maxi = (n-i) * arr[i]

print(maxi)