def solution(brown, yellow):
    answer = []
    totalTile = brown + yellow
    divide = []
    
    for i in range(2, totalTile // 2):
        if totalTile % i == 0:
            divide.append(i)

    for width in divide:
        if width == 2: continue
        
        height = totalTile / width
        
        if brown == height * 2 + width * 2 - 4:
            answer.append(height)
            answer.append(width)
            break
    
    answer.sort(reverse=True)
    return answer