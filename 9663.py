import sys
N = int(sys.stdin.readline())
isused1=[False]*N
isused2=[False]*(N+N-1)
isused3=[False]*(N+N-1)
count=0
def func(k):
    global count
    if k==N:
        count+=1
        return
    for i in range(N):
        if isused1[i] or isused2[i+k] or isused3[k-i+N-1]:
            continue
        isused1[i]=True
        isused2[i+k]=True
        isused3[k-i+N-1]=True
        func(k+1)
        isused1[i]=False
        isused2[i+k]=False
        isused3[k-i+N-1]=False 
      
func(0)
print(count)