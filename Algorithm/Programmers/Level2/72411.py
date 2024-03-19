from itertools import combinations
from collections import Counter

def solution(orders, course):
    
    answer = []
    data = []
    
    for order in orders:
        order = sorted(order)
        for c in course:
            data += combinations(order, c)
            
    value = Counter(data).most_common()
    
    myDict = {}
    for k, v in value:
        if len(k) not in myDict.keys() or myDict[len(k)] == v:
            
            if v <= 1: break
            print(k, v)
            answer.append(''.join(k))
            myDict[len(k)] = v
            
    answer = sorted(answer)
    return answer