#어차피 자연수만 주어지니까 countingSort로!
import sys

nums = int(sys.stdin.readline())
count = [0] * 10001
for i in range(nums):
    a = sys.stdin.readline()
    count[int(a)]+=1

for i in range(1,10001):
    if count[i]>=1:
        for _ in range(count[i]):
            print(i)
        