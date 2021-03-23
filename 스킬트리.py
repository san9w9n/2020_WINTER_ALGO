def solution(skill, skill_trees):
    answer = len(skill_trees)
    string=[[] for _ in range(len(skill_trees))]
    for i in range(len(skill_trees)):
        for c in skill_trees[i]:
            for j in range(len(skill)):
                if skill[j]==c:
                    string[i].append(j)

    for c in string:
        
        if c!="":
            if c!=sorted(c):
                answer-=1
            else:
                for i in range(len(c)):
                    if i!=c[i]:
                        answer-=1
                        break
                    
    return answer