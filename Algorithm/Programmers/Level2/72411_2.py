from itertools import combinations
from collections import Counter

def solution(orders, course):
    
    results = []
    
    combos = {}
    for order in orders:
        order = list(order)
        for i in range(2, len(order)+1):
            orderCombos = combinations(order, i)
            for orderCombo in orderCombos:
                key = ''.join(sorted(list(orderCombo)))
                if key in combos:
                    combos[key] += 1
                else:
                    combos[key] = 1
    
    for standard in course:
        maxValue = 0
        result = []
        for key, value in combos.items():
            if len(key) == standard and value >= 2 and value >= maxValue:
                if value == maxValue:
                    result.append(key)
                else:
                    maxValue = value
                    result = [key]
        
        results += result
    
    return sorted(results)