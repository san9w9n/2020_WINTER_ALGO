def solution(str1, str2):
    answer = 0
    arr1=dict()
    arr2=dict()
    
    str11=set()
    str22=set()
    str1=str1.lower()
    str2=str2.lower()
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str11.add(str1[i]+str1[i+1])
            try:
                arr1[str1[i]+str1[i+1]]+=1
            except:
                arr1[str1[i]+str1[i+1]]=1
                
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str22.add(str2[i]+str2[i+1])
            try:
                arr2[str2[i]+str2[i+1]]+=1
            except:
                arr2[str2[i]+str2[i+1]]=1
        
    con=list(str11.intersection(str22))
    dis=list(str22.union(str11))
    up=0
    down=0
    for e in con: 
        up+=min(arr1[e],arr2[e])
        down+=max(arr1[e],arr2[e])
    for e in dis:
        if e not in con:
            try:
                down+=arr1[e]
            except:
                down+=arr2[e]
    
    if up==0 and down==0: answer=65536
    else: answer=int((up/down)*65536)
    
    return answer