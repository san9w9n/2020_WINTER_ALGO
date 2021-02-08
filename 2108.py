import sys

N = int(sys.stdin.readline())

#-4000 ~ 4000 까지 는 총 8001개가 있다.
count=[0]*8001
total=0
many=-1
for _ in range(N):
    num = int(sys.stdin.readline())
    total+=num
    count[num+4000]+=1
    if count[num+4000]>=many: many = count[num+4000]

middle=0
maximum=-1
minimum=8001
idx=-1
arr=[]
for i in range(8001):
    if count[i]!=0 and maximum<=i: maximum=i
    if count[i]!=0 and minimum>=i: minimum=i
    if count[i]!=0:
        idx+=count[i]
    if idx>=N//2:
        idx=-600000
        middle=i-4000
    if count[i]==many:
        arr.append(i-4000)

print(round(total/N))
print(middle)
if len(arr)>1:
    print(arr[1])
else: print(arr[0])
print(maximum-minimum)

        





