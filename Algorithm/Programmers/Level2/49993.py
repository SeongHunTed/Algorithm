def solution(skill, skill_trees):
    skill = list(skill)
    answer = 0
    
    for tree in skill_trees:
        index = 0
        skillList = list(tree)
        
        for item in skillList:
            if item in skill:
                if skill[index] == item:
                    index += 1
                else:
                    index = -1
                    break
                    
        if index >= 0:
            answer += 1
            
    return answer
        
        