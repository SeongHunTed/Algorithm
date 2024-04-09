def dfs(numbers, target, index, total):
    if index == len(numbers):
        if total == target:
            return 1
        return 0
    
    case1 = dfs(numbers, target, index + 1, total + numbers[index])
    case2 = dfs(numbers, target, index + 1, total - numbers[index])
    
    return case1 + case2
    
def solution(numbers, target):
    return dfs(numbers, target, 0, 0) 