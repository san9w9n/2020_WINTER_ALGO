def solution(s):
    answer = True
    arr=[]
    check=1
    for c in s:
        if c=="(":
            arr.append(c)
        else:
            if arr and arr[-1]=="(":
                arr.pop()
            elif not arr:
                check=0
                break
                
    if check==0: return False
    elif check==1 and not arr: return True
    else: return False