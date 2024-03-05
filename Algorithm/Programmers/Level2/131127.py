import copy

def solution(want, number, discount):
    
    wishList = {}
    for i in range(len(want)):
        wishList[want[i]] = number[i]
    
    day = 0
    result = []
    while day <= (len(discount) - 10):
        lists = discount[day:day+10]
        
        day += 1
        possible = True
        for list in wishList:
            if wishList[list] != lists.count(list):
                possible = False
                break
                
        if possible:
            result.append(day)
        
        
    return len(result)
                
        