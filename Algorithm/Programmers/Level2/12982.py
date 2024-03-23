def solution(d, budget):
    answer = 0
    d.sort()
    
    total = 0
    count = 0
    for depart in d:
        if total + depart <= budget:
            total += depart
            count += 1
        else:
            return count
        
    return count