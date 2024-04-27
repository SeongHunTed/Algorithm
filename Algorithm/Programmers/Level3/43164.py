def isTransformable(a, b):
    diffCount = 0
    for i, j in zip(a, b):
        if i != j: diffCount += 1
        
    return diffCount == 1

def dfs(target, start, words, count, visited):
    # 같은 단어면 종료
    if target == start:
        return count
    
    result = float('inf')
    for index, word in enumerate(words):
        if not visited[index]:
            if isTransformable(word, start):
                visited[index] = 1
                result = min(dfs(target, word, words, count + 1, visited), result)
                visited[index] = 0
                
    return result
        

def solution(begin, target, words):
    
    results = []
    
    # 없는 경우 return
    if target not in words:
        return 0
    
    for index, word in enumerate(words):
        visited = [0] * len(words)
        if isTransformable(word, begin):
            visited[index] = 1
            answer = dfs(target, word, words, 1, visited)
            results.append(answer)
            visited[index] = 0
    
    return min(results)
            
    