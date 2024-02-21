def solution(elements):
    answer = 0
    n = 0
    elementLength = len(elements)
    results = []
    
    while n != elementLength:
        n += 1
        for i in range(elementLength):
            if i + n > elementLength:
                results.append(sum(elements[i:]) + sum(elements[:i+n-elementLength]))
            else:
                results.append(sum(elements[i:i+n]))
            
    answer = len(set(results))
    
    return answer