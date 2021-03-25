n=10000000
a = [False,False] + [True]*(n-1)

for i in range(2,n+1):
    if a[i]:
        for j in range(2*i, n+1, i):
            a[j] = False

def solution(numbers):
    answer = 0
    counting=[0]+[0]*9
    comp=[0]+[0]*9
    for c in numbers: counting[int(c)]+=1
    
    print(counting)
    for i in range(int('9'*len(numbers))+1):
        comp=[0]+[0]*9
        out=1
        if a[i]:
            for num in str(i):
                comp[int(num)]+=1
            
            for i in range(10):
                if counting[i] < comp[i]:
                    out=0
            if out==1: answer+=1
    
    
    return answer