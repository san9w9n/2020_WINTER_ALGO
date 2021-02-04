import sys

n = sys.stdin.readline()
arr=[]
for i in range(len(n)-1):
    arr.append(int(n[i]))

arr.sort()

for i in range(len(n)-1):
    arr[i] = str(arr[i])
string = ""
for i in range(len(n)-2,-1,-1):
    string+=arr[i]

print(string)