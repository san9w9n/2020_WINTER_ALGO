#N개의 정수로 이루어진 수열이 있을 때,
#크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이
#S가 되는 경우의 수를 구해야한다.
from itertools import combinations 

num, s = map(int, input().split())
arr = list(map(int,input().split()))
subset = []
for i in range(0,len(arr)+1):
    set_arr = combinations(arr,i)
    #combinations(array, int)
    #array안에 있는 요소들을 인자로 준 i만큼 부분집합을 구해준다.
    #i길이의 조합의 모든 경우의 수를 구해주는 것이다.

    subset.extend(set_arr)

sum_set = []
for i in range(1,len(subset)):
    sum_set.append(sum(subset[i]))

count=0
for x in sum_set:
    if x==s:
        count+=1

print(count)