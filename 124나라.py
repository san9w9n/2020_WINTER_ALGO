def solution(n):
    answer = ''
    
    dap=['1','2','4']
    n-=1
    if n==0: return '1'
    a,i=0,1
    while a+3**i<=n:
        a+=3**i
        i+=1
    n-=a
    arr=[]
    for idx in range(i):
        arr.append(n%3)
        n//=3
    print(arr)
    for idx in arr:
        answer=dap[idx]+answer
    
    return answer