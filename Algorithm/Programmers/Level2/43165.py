def dfs(n, order, numbers, target):
    if order == len(numbers) - 1:
        if target == n:
            return 1
    
        return 0
    
    case1 = dfs(n+numbers[order+1], order+1, numbers, target)
    case2 = dfs(n-numbers[order+1], order+1, numbers, target)
    
    return case1 + case2

def solution(numbers, target):
    return dfs(numbers[0], 0, numbers, target) + dfs(-numbers[0], 0, numbers, target)