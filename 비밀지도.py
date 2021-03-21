def binary(n,num):
    string=''
    for i in range(n):
        string=str(num%2)+string
        num//=2
    return string

def solution(n, arr1, arr2):
    answer = [[' ' for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        string=binary(n,arr1[i])
        for j in range(n):
            if string[j]=='1': answer[i][j]='#'
    
    for i in range(n):
        string=binary(n,arr2[i])
        for j in range(n):
            if string[j]=='1': answer[i][j]='#'
    
    arr=[]
    for i in range(n):
        arr.append(''.join(map(str,answer[i])))

    return arr