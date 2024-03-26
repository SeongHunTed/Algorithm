# 누적합
def solution(topping):
    answer = 0
    
    chul = {}
    for item in topping:
        if item in chul.keys():
            chul[item] += 1
        else:
            chul[item] = 1
            
    brother = set()
    for i in range(0, len(topping)):
        item = topping[i]
        brother.add(item)
        chul[item] -= 1
        
        if chul[item] == 0: 
            chul.pop(item)
        
        if len(chul) == len(brother):
            answer += 1
    
    if answer > 0: return answer
    return 0