def solution(files):
    answer = []
    spl = [["" for _ in range(4)] for _ in range(len(files))]
    for i in range(len(files)):
        spl[i][0]=i
        check=0
        for c in files[i]:
            if c==".":
                spl[i][3]+=files[i].split('.')[1]
                break
            elif check==0 and (c.isalpha() or c=="-" or c==" "): spl[i][1]+=c.lower()
            elif c.isdecimal():
                check=1
                spl[i][2]+=c
    
    for i in range(len(spl)):
        spl[i][2]=int(spl[i][2])
    
    spl.sort(key=lambda x:x[2])
    spl.sort(key=lambda x:x[1])
    
    for e in spl:
        answer.append(files[e[0]])
    return answer